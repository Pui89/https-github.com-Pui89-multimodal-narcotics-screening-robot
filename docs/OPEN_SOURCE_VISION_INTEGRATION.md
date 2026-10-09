# DINOv2 + Anomalib: end-to-end integration baseline

This is an optional, fail-closed software integration layer, not a validated narcotics detector.

## Models

- [DINOv2](https://github.com/facebookresearch/dinov2): generic visual embeddings for downstream comparison/retrieval. It does **not** identify chemical composition.
- [Anomalib](https://github.com/open-edge-platform/anomalib): anomaly scoring for distribution shift or unusual visual appearance. Anomaly is not evidence that a substance is illegal or hazardous.

## Layout and flow

```text
Image / inspection frame
  -> application-specific preprocessing and quality checks
  -> optional DINOv2 embedding and/or Anomalib score
  -> make_screening_record(score, threshold)
  -> verify_screening_record(record)
  -> mandatory qualified human review
  -> separately authorized safety controller (not implemented here)
```

Install compatible versions of PyTorch, Transformers and Anomalib separately according to their official instructions. No model weights are downloaded or loaded by importing `pui89_vision`; inject loaded model/processor/predictor objects explicitly. Check exact code, checkpoint and dependency licenses before redistribution or commercial use.

## Quick start (model-independent verification)

```python
from pui89_vision import make_screening_record, verify_screening_record
record = make_screening_record("anomalib-baseline", 0.73, threshold=0.5)
assert verify_screening_record(record)
assert record.human_review_required and not record.actuator_authorized
```

The score is a triage signal only. Thresholds require validation on representative, independently held-out data; do not present them as calibrated probabilities. Missing scores abstain. Invalid/non-finite/out-of-range scores are rejected. The evidence ID is an unkeyed SHA-256 integrity checksum, **not** a digital signature or tamper-proof audit log. Production requires access-controlled append-only storage, trusted timestamps, key-managed signatures, model/version capture, and a threat model.

## End-to-end verification and benchmark

Run `python -m unittest discover -s tests -v`. These tests cover record integrity and fail-safe flags, not the accuracy of downloaded models. Report precision/recall, false-alarm rate, calibration, abstention coverage, latency, memory, performance by environment and sensor quality, and version/license details. No accuracy or field-readiness claim is made by this baseline.

For real chemical screening, validated spectroscopy (for example Raman or FTIR where appropriate), reference standards, chain-of-custody procedures and qualified human confirmation are required. Never use a generic visual model as chemical evidence or directly connect this package to actuation.
