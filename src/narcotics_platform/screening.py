from dataclasses import dataclass
from typing import Any

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

class ScreeningPipeline:
    def __init__(self, threshold: float = 0.60) -> None:
        if not 0 <= threshold <= 1:
            raise ValueError('threshold must be between 0 and 1')
        self.threshold = threshold

    @staticmethod
    def normalize_label(label: str) -> str:
        return label if label in SUPPORTED_CLASSES else 'unknown_substance'

    def screen(self, detections: list[dict[str, Any]]) -> ScreeningResult:
        candidates = []
        for d in detections:
            confidence = float(d.get('confidence', 0.0))
            if not 0 <= confidence <= 1 or confidence < self.threshold:
                continue
            candidates.append(Candidate(self.normalize_label(str(d.get('label', 'unknown'))), confidence, str(d.get('source', 'vision'))))
        if not candidates:
            return ScreeningResult('UNKNOWN', [])
        return ScreeningResult('HUMAN_REVIEW', candidates)
