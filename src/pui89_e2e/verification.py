"""Independent integrity and safety-invariant checks for pipeline outputs."""
from __future__ import annotations

from dataclasses import asdict, dataclass
import hashlib
import json
from typing import Any

from .pipeline import PipelineResult


@dataclass(frozen=True)
class VerificationReport:
    valid: bool
    checks: dict[str, bool]
    errors: list[str]
    evidence_id: str | None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _digest(payload: dict[str, Any]) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str).encode()
    return "ev-" + hashlib.sha256(encoded).hexdigest()[:16]


def verify_pipeline_result(result: PipelineResult | dict[str, Any]) -> VerificationReport:
    """Check output/audit consistency, evidence ID integrity, and fail-safe invariants.

    This detects accidental or unsophisticated tampering; a short unkeyed hash is
    not a digital signature and does not authenticate who created a record.
    """
    data = result.to_dict() if isinstance(result, PipelineResult) else result
    errors: list[str] = []
    checks: dict[str, bool] = {}
    audit = data.get("audit_record")

    checks["audit_record_present"] = isinstance(audit, dict)
    if not checks["audit_record_present"]:
        errors.append("audit_record_missing")
        return VerificationReport(False, checks, errors, data.get("evidence_id"))

    payload_keys = (
        "case_id", "status", "hypothesis", "confidence", "observations",
        "accepted_sensor_ids", "reasons", "timestamp",
    )
    payload = {key: audit.get(key) for key in payload_keys}
    expected_id = _digest(payload)
    actual_id = data.get("evidence_id")
    checks["evidence_id_matches_payload"] = actual_id == expected_id and audit.get("evidence_id") == expected_id
    if not checks["evidence_id_matches_payload"]:
        errors.append("evidence_id_integrity_check_failed")

    mirrored = {
        "status_matches": (data.get("status"), audit.get("status")),
        "hypothesis_matches": (data.get("screening_hypothesis"), audit.get("hypothesis")),
        "confidence_matches": (data.get("confidence"), audit.get("confidence")),
        "timestamp_matches": (data.get("timestamp"), audit.get("timestamp")),
        "accepted_count_matches": (data.get("accepted_observations"), audit.get("accepted_observations")),
        "rejected_count_matches": (data.get("rejected_observations"), audit.get("rejected_observations")),
        "modalities_match": (data.get("modalities"), audit.get("modalities")),
    }
    for name, (left, right) in mirrored.items():
        checks[name] = left == right
        if not checks[name]:
            errors.append(name)

    checks["human_review_mandatory"] = (
        data.get("human_review_required") is True and audit.get("human_review_required") is True
    )
    if not checks["human_review_mandatory"]:
        errors.append("human_review_must_remain_required")

    checks["robot_motion_not_authorized"] = (
        data.get("robot_motion_authorized") is False and audit.get("robot_motion_authorized") is False
    )
    if not checks["robot_motion_not_authorized"]:
        errors.append("robot_motion_must_not_be_authorized_by_screening_pipeline")

    checks["observation_counts_nonnegative"] = (
        isinstance(data.get("accepted_observations"), int)
        and isinstance(data.get("rejected_observations"), int)
        and data.get("accepted_observations", -1) >= 0
        and data.get("rejected_observations", -1) >= 0
    )
    if not checks["observation_counts_nonnegative"]:
        errors.append("invalid_observation_counts")

    checks["confidence_in_range"] = (
        isinstance(data.get("confidence"), (int, float))
        and 0.0 <= data.get("confidence", -1.0) <= 1.0
    )
    if not checks["confidence_in_range"]:
        errors.append("confidence_out_of_range")

    checks["known_status"] = data.get("status") in {"HUMAN_REVIEW", "ABSTAIN"}
    if not checks["known_status"]:
        errors.append("unknown_pipeline_status")

    checks["abstain_means_unknown"] = (
        data.get("status") != "ABSTAIN" or (
            data.get("screening_hypothesis") == "unknown_substance"
            and data.get("confidence") == 0.0
        )
    )
    if not checks["abstain_means_unknown"]:
        errors.append("abstention_must_preserve_unknown")

    return VerificationReport(
        valid=all(checks.values()),
        checks=checks,
        errors=errors,
        evidence_id=actual_id,
    )
