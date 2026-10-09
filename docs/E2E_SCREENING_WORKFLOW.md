# Executable end-to-end object screening workflow

This reference implements a reproducible data-contract vertical slice: case validation -> modality quality/OOD gates -> evidence fusion -> disagreement/threshold handling -> review-queue report -> integrity verification -> tests and CI.

## Run

```bash
python -m unittest discover -s tests -p 'test_e2e_screening.py' -v
python -m e2e_screening.workflow --input examples/synthetic_screening_case.json --output screening-report.json
```

The sample is synthetic. Inputs are scores supplied by external, separately validated modality adapters; this code does not contain or validate a narcotics detector. The unweighted mean is a transparent baseline and **not a calibrated probability**. Thresholds must be validated against representative, lawfully collected data and false-positive/false-negative costs.

## Safety, privacy and operational boundary

Only objects/containers are accepted; person screening is explicitly rejected. The workflow does not infer ingestion, identify people, confirm substance presence, or authorize searches, seizures, detention, or other enforcement. Every output requires qualified human review and has `automated_enforcement_decision=false`. Use documented consent/legal authority, data minimization, retention limits, access control, audit, independent validation, and appeal/escalation procedures. A positive screen is a lead for confirmatory testing by authorized personnel, never proof.

## Benchmark plan (do not claim results before running)

Use sealed train/validation/test splits with site/device separation. Report sensitivity, specificity, precision, recall, PR-AUC, false-positive rate at fixed sensitivity, calibration error, abstention rate, per-modality contribution, disagreement rate, latency, and subgroup/environment stratification where lawful and appropriate. Publish confidence intervals, data provenance, protocol, and failure cases. Include sensor failure, low-quality, out-of-distribution, conflicting modalities, and threshold perturbation tests.
