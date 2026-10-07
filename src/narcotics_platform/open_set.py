from dataclasses import dataclass

@dataclass(frozen=True)
class OpenSetDecision:
    known: bool
    label: str
    ood_score: float
    abstain: bool
    reason: str

def classify_open_set(label: str, confidence: float, ood_score: float, confidence_threshold: float = 0.60, ood_threshold: float = 0.50) -> OpenSetDecision:
    if any(not 0.0 <= v <= 1.0 for v in (confidence, ood_score)): raise ValueError("scores must be between 0 and 1")
    if confidence < confidence_threshold or ood_score >= ood_threshold:
        reason = "insufficient confidence" if confidence < confidence_threshold else "possible unknown / out-of-distribution observation"
        return OpenSetDecision(False, "unknown_substance", ood_score, True, reason)
    return OpenSetDecision(True, label, ood_score, False, "within configured screening envelope")