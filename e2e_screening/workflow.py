"""Evidence-aware, human-reviewed object screening reference; never an enforcement decision."""
from __future__ import annotations
import argparse, hashlib, json, math
from pathlib import Path
from typing import Any

ALLOWED_MODALITIES = {"rgb", "nir", "thermal", "depth", "xray_metadata", "chemical_sensor_metadata"}

def _digest(value: dict[str, Any]) -> str:
    clean = dict(value); clean.pop("integrity_sha256", None)
    return hashlib.sha256(json.dumps(clean, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()).hexdigest()

def screen_case(case: dict[str, Any]) -> dict[str, Any]:
    """Fuse externally produced modality scores into a review queue item.

    Scores are screening signals, not proof that a substance is present. This module does not
    process people, infer ingestion, identify individuals, or authorize searches/seizures.
    """
    if not isinstance(case, dict) or not isinstance(case.get("case_id"), str) or not case["case_id"].strip():
        raise ValueError("case_id must be a non-empty string")
    if case.get("subject_type") != "object_or_container":
        raise ValueError("only object_or_container screening is supported")
    observations = case.get("observations")
    if not isinstance(observations, list):
        raise ValueError("observations must be a list")
    quality_min = case.get("minimum_quality", 0.5)
    ood_max = case.get("maximum_ood_score", 0.5)
    threshold = case.get("review_threshold", 0.65)
    for name, val in (("minimum_quality", quality_min), ("maximum_ood_score", ood_max), ("review_threshold", threshold)):
        if not isinstance(val, (int, float)) or isinstance(val, bool) or not math.isfinite(val) or not 0 <= val <= 1:
            raise ValueError(name + " must be in [0,1]")
    accepted, rejected = [], []
    seen = set()
    for o in observations:
        if not isinstance(o, dict): raise ValueError("each observation must be an object")
        modality = o.get("modality")
        if modality not in ALLOWED_MODALITIES: raise ValueError("unsupported modality: " + str(modality))
        if modality in seen: raise ValueError("duplicate modality records are not accepted")
        seen.add(modality)
        score, quality, ood = o.get("screening_score"), o.get("quality_score"), o.get("ood_score")
        for name, val in (("screening_score", score), ("quality_score", quality), ("ood_score", ood)):
            if not isinstance(val, (int, float)) or isinstance(val, bool) or not math.isfinite(val) or not 0 <= val <= 1:
                raise ValueError(name + " must be in [0,1]")
        if quality < quality_min: rejected.append({"modality": modality, "reason": "LOW_QUALITY"})
        elif ood > ood_max: rejected.append({"modality": modality, "reason": "OUT_OF_DISTRIBUTION"})
        else: accepted.append({"modality": modality, "screening_score": float(score), "quality_score": float(quality), "ood_score": float(ood)})
    min_modalities = case.get("minimum_modalities", 2)
    if not isinstance(min_modalities, int) or isinstance(min_modalities, bool) or min_modalities < 1:
        raise ValueError("minimum_modalities must be a positive integer")
    if len(accepted) < min_modalities:
        status, reason, fused = "ABSTAIN_INSUFFICIENT_EVIDENCE", "TOO_FEW_VALID_MODALITIES", None
    else:
        # Transparent unweighted mean: a reference baseline, not a calibrated probability.
        fused = sum(o["screening_score"] for o in accepted) / len(accepted)
        if max(o["screening_score"] for o in accepted) - min(o["screening_score"] for o in accepted) > float(case.get("maximum_score_disagreement", 0.45)):
            status, reason = "HUMAN_REVIEW_CONFLICTING_EVIDENCE", "MODALITY_DISAGREEMENT"
        elif fused >= threshold:
            status, reason = "HUMAN_REVIEW_FLAG", "SCREENING_THRESHOLD_EXCEEDED"
        else:
            status, reason = "HUMAN_REVIEW_NO_FLAG", "BELOW_SCREENING_THRESHOLD"
    report = {"schema_version": "1.0", "case_id": case["case_id"], "subject_type": "object_or_container",
              "status": status, "reason": reason, "fused_screening_score": fused,
              "accepted_evidence": accepted, "rejected_evidence": rejected,
              "human_review_required": True, "automated_enforcement_decision": False,
              "substance_presence_confirmed": False, "individual_risk_inference": False}
    report["integrity_sha256"] = _digest(report)
    return report

def verify_report(report: dict[str, Any]) -> bool:
    return isinstance(report, dict) and isinstance(report.get("integrity_sha256"), str) and report["integrity_sha256"] == _digest(report)

def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True); p.add_argument("--output", required=True)
    a = p.parse_args()
    report = screen_case(json.loads(Path(a.input).read_text(encoding="utf-8")))
    Path(a.output).write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status": report["status"], "output": a.output, "integrity_ok": verify_report(report)}))
if __name__ == "__main__": main()
