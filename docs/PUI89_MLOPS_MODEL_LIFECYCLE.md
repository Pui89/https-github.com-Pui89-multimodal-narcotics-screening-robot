# PUI89 MLOps and Model Lifecycle

Dataset → Version → Training → Validation → Robustness/OOD → Calibration → Safety review → Approval → Deployment → Monitoring → Failure analysis → Retraining.

## Registry fields
model_id, task, dataset_version, training commit, checksum, hardware, latency, memory, accuracy, calibration, OOD metrics, limitations, license, approval state and deployment history.

## Monitoring
Latency, dropped frames, sensor health, synchronization drift, confidence, uncertainty, OOD score, abstention, review rate, safety interventions and mission outcomes.

## Release gate
Higher accuracy alone is insufficient. Require robustness, calibration, OOD/abstention, safety regression, license/supply-chain and reproducibility checks.
