"""Reproducible JSONL evaluation runner.

Input records require: y_true, y_pred, confidence, correct.
No benchmark values are embedded in the repository.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from metrics import classification_metrics, expected_calibration_error


def load_jsonl(path: Path) -> list[dict]:
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def evaluate(rows: list[dict]) -> dict:
    y_true = [r["y_true"] for r in rows]
    y_pred = [r["y_pred"] for r in rows]
    confidence = [float(r["confidence"]) for r in rows]
    correct = [bool(r.get("correct", a == b)) for r, a, b in zip(rows, y_true, y_pred)]
    m = classification_metrics(y_true, y_pred)
    return {
        "n": len(rows),
        "accuracy": m.accuracy,
        "precision": m.precision,
        "recall": m.recall,
        "f1": m.f1,
        "ece": expected_calibration_error(confidence, correct),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path, default=Path("reports/evaluation.json"))
    args = parser.parse_args()
    result = evaluate(load_jsonl(args.input))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
