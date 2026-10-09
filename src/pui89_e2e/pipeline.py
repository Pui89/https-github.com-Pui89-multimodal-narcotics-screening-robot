"""Deterministic end-to-end screening workflow reference implementation.

Consumes normalized sensor/perception observations. It does not identify chemical
composition, replace a validated detector, or command robot actuators.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
import hashlib
import json
from typing import Any, Iterable


@dataclass(frozen=True)
class SensorObservation:
    sensor_id: str
    modality: str
    timestamp: str
    quality: float
    candidate_label: str = "unknown_substance"
    confidence: float = 0.0
    track_id: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class PipelineConfig:
    min_sensor_quality: float = 0.5
    min_candidate_confidence: float = 0.65
    min_independent_modalities: int = 2
    max_timestamp_skew_seconds: float = 2.0
    allowed_labels: tuple[str, ...] = (
        "amphetamine", "heroin", "methamphetamine_crystal",
        "narcotic_unknown", "unknown_substance",
    )


@dataclass
class PipelineResult:
    status: str
    screening_hypothesis: str
    confidence: float
    accepted_observations: int
    rejected_observations: int
    modalities: list[str]
    reasons: list[str]
    human_review_required: bool
    robot_motion_authorized: bool
    evidence_id: str
    timestamp: str
    audit_record: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _parse_timestamp(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    return parsed if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)


def _stable_evidence_id(payload: dict[str, Any]) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str).encode()
    return "ev-" + hashlib.sha256(encoded).hexdigest()[:16]


class EndToEndScreeningPipeline:
    """Quality gate → evidence fusion → abstention → review → audit.

    This is an executable software baseline, not a validated narcotics detector.
    All results require human review; no actuator interface is exposed.
    """

    def __init__(self, config: PipelineConfig | None = None):
        self.config = config or PipelineConfig()

    def run(
        self,
        observations: Iterable[SensorObservation | dict[str, Any]],
        *,
        case_id: str | None = None,
        now: str | None = None,
    ) -> PipelineResult:
        received = [
            item if isinstance(item, SensorObservation) else SensorObservation(**item)
            for item in observations
        ]
        run_time = now or _utc_now()
        reasons: list[str] = []
        accepted: list[SensorObservation] = []
        rejected = 0

        for obs in received:
            reason = None
            if not obs.sensor_id or not obs.modality:
                reason = "missing_sensor_identity_or_modality"
            elif not 0.0 <= obs.quality <= 1.0:
                reason = "invalid_quality_range"
            elif not 0.0 <= obs.confidence <= 1.0:
                reason = "invalid_confidence_range"
            elif obs.quality < self.config.min_sensor_quality:
                reason = "sensor_quality_below_threshold"
            else:
                try:
                    _parse_timestamp(obs.timestamp)
                except (ValueError, TypeError):
                    reason = "invalid_timestamp"
            if reason:
                rejected += 1
                reasons.append(f"{obs.sensor_id or 'unknown_sensor'}:{reason}")
            else:
                accepted.append(obs)

        if accepted:
            times = [_parse_timestamp(x.timestamp) for x in accepted]
            if (max(times) - min(times)).total_seconds() > self.config.max_timestamp_skew_seconds:
                rejected += len(accepted)
                reasons.append("temporal_alignment_failed")
                accepted = []

        modalities = sorted({x.modality.lower() for x in accepted})
        label_scores: dict[str, list[float]] = {}
        for obs in accepted:
            label = obs.candidate_label
            if label not in self.config.allowed_labels:
                reasons.append(f"{obs.sensor_id}:label_not_in_taxonomy")
                continue
            if label != "unknown_substance" and obs.confidence >= self.config.min_candidate_confidence:
                label_scores.setdefault(label, []).append(obs.confidence * obs.quality)

        winner, winner_score = None, 0.0
        if label_scores:
            winner, winner_score = sorted(
                ((label, sum(scores) / len(scores)) for label, scores in label_scores.items()),
                key=lambda pair: (-pair[1], pair[0]),
            )[0]

        enough_modalities = len(modalities) >= self.config.min_independent_modalities
        if not accepted:
            status, hypothesis, confidence = "ABSTAIN", "unknown_substance", 0.0
            reasons.append("no_usable_sensor_evidence")
        elif not enough_modalities:
            status, hypothesis, confidence = "HUMAN_REVIEW", winner or "unknown_substance", round(winner_score, 4)
            reasons.append("insufficient_independent_modalities")
        elif winner is None:
            status, hypothesis, confidence = "HUMAN_REVIEW", "unknown_substance", 0.0
            reasons.append("no_supported_screening_hypothesis")
        else:
            status, hypothesis, confidence = "HUMAN_REVIEW", winner, round(winner_score, 4)
            reasons.append("screening_hypothesis_requires_human_verification")

        evidence_payload = {
            "case_id": case_id,
            "status": status,
            "hypothesis": hypothesis,
            "confidence": confidence,
            "observations": [asdict(x) for x in received],
            "accepted_sensor_ids": [x.sensor_id for x in accepted],
            "reasons": reasons,
            "timestamp": run_time,
        }
        evidence_id = _stable_evidence_id(evidence_payload)
        audit_record = {
            **evidence_payload,
            "evidence_id": evidence_id,
            "accepted_observations": len(accepted),
            "rejected_observations": rejected,
            "modalities": modalities,
            "human_review_required": True,
            "robot_motion_authorized": False,
            "disclaimer": (
                "A screening hypothesis is not chemical identification or proof. "
                "Human verification using validated procedures is required."
            ),
        }
        return PipelineResult(
            status=status,
            screening_hypothesis=hypothesis,
            confidence=confidence,
            accepted_observations=len(accepted),
            rejected_observations=rejected,
            modalities=modalities,
            reasons=reasons,
            human_review_required=True,
            robot_motion_authorized=False,
            evidence_id=evidence_id,
            timestamp=run_time,
            audit_record=audit_record,
        )
