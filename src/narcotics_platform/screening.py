from dataclasses import dataclass
from typing import Any
from .open_set import classify_open_set
from .uncertainty import estimate_uncertainty
from .fusion import ModalityEvidence, MultimodalFusion

SUPPORTED_CLASSES = ('amphetamine', 'heroin', 'methamphetamine_crystal', 'narcotic_unknown', 'unknown_substance')

@dataclass(frozen=True)
class Candidate:
    label: str
    confidence: float
    source: str = 'vision'

@dataclass(frozen=True)
class ScreeningResult:
    state: str
    candidates: list[Candidate]
    requires_human_review: bool = True
    note: str = 'Screening hypothesis only; not forensic chemical identification or internal-body diagnosis.'
    uncertainty: float = 1.0
    ood_score: float = 0.0
    modality_agreement: float = 0.0
    abstained: bool = True

class ScreeningPipeline:
    def __init__(self, threshold: float = 0.60) -> None:
        if not 0 <= threshold <= 1: raise ValueError('threshold must be between 0 and 1')
        self.threshold = threshold
        self.fusion = MultimodalFusion()

    @staticmethod
    def normalize_label(label: str) -> str:
        return label if label in SUPPORTED_CLASSES else 'unknown_substance'

    def screen(self, detections: list[dict[str, Any]], *, sensor_quality: float = 1.0, ood_score: float = 0.0) -> ScreeningResult:
        evidence = []
        for d in detections:
            confidence = float(d.get('confidence', 0.0))
            if not 0 <= confidence <= 1: continue
            evidence.append(ModalityEvidence(str(d.get('modality', d.get('source', 'vision'))), self.normalize_label(str(d.get('label', 'unknown'))), confidence, float(d.get('quality', 1.0)), str(d.get('source_id', '')) or None))
        fused = self.fusion.fuse(evidence)
        decision = classify_open_set(fused.label, fused.confidence, ood_score, self.threshold)
        uncertainty = estimate_uncertainty(fused.confidence, fused.agreement, sensor_quality, ood_score)
        candidates = [Candidate(decision.label, fused.confidence, ','.join(fused.contributing_modalities) or 'none')] if evidence else []
        state = 'ABSTAIN' if decision.abstain else 'HUMAN_REVIEW'
        return ScreeningResult(state, candidates, True, uncertainty.calibration_status + ': screening hypothesis only; not chemical identification.', uncertainty.uncertainty, ood_score, fused.agreement, decision.abstain)