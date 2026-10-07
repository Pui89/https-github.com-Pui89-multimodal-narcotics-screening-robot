from dataclasses import dataclass

@dataclass(frozen=True)
class UncertaintyEstimate:
    confidence: float
    uncertainty: float
    calibration_status: str
    reasons: tuple[str, ...]

def estimate_uncertainty(confidence: float, agreement: float, sensor_quality: float, ood_score: float = 0.0) -> UncertaintyEstimate:
    values = (confidence, agreement, sensor_quality, ood_score)
    if any(not 0.0 <= value <= 1.0 for value in values): raise ValueError("all inputs must be between 0 and 1")
    adjusted = confidence * (0.5 + 0.5 * agreement) * sensor_quality * (1.0 - 0.7 * ood_score)
    adjusted = max(0.0, min(1.0, adjusted))
    reasons: list[str] = []
    if agreement < 0.5: reasons.append("cross-modal disagreement")
    if sensor_quality < 0.5: reasons.append("degraded sensor quality")
    if ood_score >= 0.5: reasons.append("possible out-of-distribution observation")
    status = "CALIBRATED_BASELINE" if not reasons else "DEGRADED_REVIEW"
    return UncertaintyEstimate(adjusted, 1.0-adjusted, status, tuple(reasons))