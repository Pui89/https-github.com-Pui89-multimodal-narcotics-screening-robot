from dataclasses import dataclass
from typing import Sequence

@dataclass(frozen=True)
class ClassificationMetrics:
    accuracy: float
    precision: float
    recall: float
    f1: float

def classification_metrics(y_true: Sequence[str], y_pred: Sequence[str], positive_label: str | None = None) -> ClassificationMetrics:
    if len(y_true) != len(y_pred) or not y_true: raise ValueError("inputs must be non-empty and equal length")
    accuracy = sum(a == b for a,b in zip(y_true,y_pred)) / len(y_true)
    if positive_label is None: positive_label = sorted(set(y_true) | set(y_pred))[0]
    tp = sum(a == positive_label and b == positive_label for a,b in zip(y_true,y_pred))
    fp = sum(a != positive_label and b == positive_label for a,b in zip(y_true,y_pred))
    fn = sum(a == positive_label and b != positive_label for a,b in zip(y_true,y_pred))
    precision = tp/(tp+fp) if tp+fp else 0.0
    recall = tp/(tp+fn) if tp+fn else 0.0
    f1 = 2*precision*recall/(precision+recall) if precision+recall else 0.0
    return ClassificationMetrics(accuracy, precision, recall, f1)

def expected_calibration_error(confidences: Sequence[float], correct: Sequence[bool], bins: int = 10) -> float:
    if len(confidences) != len(correct) or not confidences: raise ValueError("inputs must be non-empty and equal length")
    total, error = len(confidences), 0.0
    for i in range(bins):
        lo, hi = i/bins, (i+1)/bins
        members = [j for j,c in enumerate(confidences) if lo <= c < hi or (i == bins-1 and c == hi)]
        if members:
            avg_conf = sum(confidences[j] for j in members)/len(members)
            avg_acc = sum(bool(correct[j]) for j in members)/len(members)
            error += len(members)/total * abs(avg_conf-avg_acc)
    return error