# Dataset and Annotation Standard

The dataset layer is designed for lawful, authorized external-object/environment screening. It is not a medical or forensic chemistry dataset.

## Sample record

Use JSONL records validated against `schemas/screening_event.schema.json`.

Record:
- event/time identifiers
- available modalities and synchronization state
- 2D/3D evidence references
- calibration and model versions
- reviewer status
- provenance and retention policy

## Annotation rules

1. Annotate only observable evidence.
2. Never label internal-body state or ingestion from ordinary sensor observations.
3. Use `unknown_substance` or `unlabeled` when evidence is insufficient.
4. Missing modalities are recorded as missing, not as negative evidence.
5. Separate machine predictions from human-reviewed outcomes.
6. Do not include unnecessary personal identifiers.
7. Keep dataset versioning and provenance with every evaluation run.

## Recommended splits

Use fixed, documented train/validation/test splits. Keep source sessions separated where possible to reduce leakage across nearly identical frames.

## Benchmark principle

A benchmark should test both recognition and safe abstention: the system should be rewarded for identifying unfamiliar or ambiguous observations as unknown/review rather than forcing a confident class.
