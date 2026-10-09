# Reproducible Screening Benchmarks and Next-Stage Build Plan

Status: evaluation tooling and protocol; not a validated detection system.

## Main engineering gap

The reference pipeline consumes normalized observations and candidate labels/confidence values. That is useful for testing the downstream workflow, but it is not a raw-sensor narcotics detector and does not establish chemical identity. The next research step is to evaluate permitted, clearly scoped external-object/environment screening on labelled, legally collected data, with false positives, uncertainty and human-review behavior measured explicitly.

This project must not be used to diagnose ingestion or internal-body concealment, identify people by demographic traits, or autonomously enforce, detain, seize or accuse. A model output is a screening hypothesis only.

## Added benchmark metadata gate

`tools/validate_benchmark_report.py` uses only the Python standard library. It rejects missing provenance, placeholder text, timestamps without a timezone and non-numeric/non-finite metric values.

```bash
python tools/validate_benchmark_report.py benchmarks/reports/screening-run.json
pytest -q tests/test_benchmark_report_validator.py
```

This is a metadata-quality check, not proof of detection performance, forensic validity or system safety. Do not commit fabricated metrics. Record dataset governance, lawful collection basis, labeler protocol, model/checkpoint hash, exact Git commit, hardware and run configuration.

## Minimum evaluation matrix

| Scenario | Required measurement |
|---|---|
| Held-out authorized test objects/scenes | per-class precision, recall, F1, confusion matrix |
| Non-target objects and ordinary clutter | false-positive rate and false alarms per hour/session |
| Unseen objects / out-of-distribution scenes | unknown detection, abstention rate and error rate among non-abstained cases |
| Sensor disagreement or missing modality | fault detection, confidence change and correct human-review trigger |
| Blur, low light, glare, occlusion, motion | metrics by condition, not only overall average |
| Calibration | reliability diagram, Brier score or ECE with stated method |
| Repeated sessions/sites | site-held-out generalization and confidence intervals |
| Edge hardware | p50/p95 latency, throughput, memory and power |
| Audit pipeline | provenance completeness, tamper-detection tests, reviewer identity/access audit |
| Human review | inter-reviewer agreement and overturn rate where ethically and lawfully collected |

Do not use synthetic examples as a substitute for independent test data. Split by scene/site/session to avoid near-duplicate leakage. Report base rates and false-positive costs; do not imply a positive visual screen proves a substance's chemical identity.

## Open-source stack to evaluate

Confirm versions, model-weight terms and dataset licenses independently; the repository license does not automatically cover third-party weights/data.

- ROS 2 (Apache-2.0): https://github.com/ros2/ros2 — sensor interfaces, lifecycle and robot integration.
- Navigation2 (Apache-2.0): https://github.com/ros-navigation/navigation2 — safe navigation/recovery integration where mobile navigation is used.
- Gazebo Sim (Apache-2.0): https://github.com/gazebosim/gz-sim — simulation and fault injection.
- Open3D (MIT): https://github.com/isl-org/Open3D — 3D geometry and point-cloud processing.
- OpenCV (Apache-2.0): https://github.com/opencv/opencv — image acquisition and processing.
- Anomalib (Apache-2.0): https://github.com/openvinotoolkit/anomalib — visual anomaly detection baselines; not a chemical identifier.
- DINOv2 (Apache-2.0): https://github.com/facebookresearch/dinov2 — visual representations for controlled evaluation.
- FiftyOne (Apache-2.0): https://github.com/voxel51/fiftyone — dataset curation and error analysis.
- DVC (Apache-2.0): https://github.com/iterative/dvc — data and experiment versioning.
- MLflow (Apache-2.0): https://github.com/mlflow/mlflow — experiment tracking and artifact lineage.
- OpenSSF Scorecard (Apache-2.0): https://github.com/ossf/scorecard — software supply-chain posture.

These are candidates to evaluate, not a claim they are integrated. A visual anomaly model can flag unusual appearance; it cannot establish chemical composition.

## Evidence security and human review

The existing unkeyed evidence digest is useful for consistency checks but is not a signature or identity proof. Next, define a versioned canonical evidence schema, hash the exact serialized payload, use authenticated signing keys held outside the application process, restrict evidence access with roles, record reviewer decisions and test tamper detection. Key rotation, retention, access logging and privacy review must be documented. A signature authenticates the record source; it does not make the model's prediction true.

## Release gates

1. Every positive/uncertain screen remains a human-reviewed hypothesis.
2. Unknown, low-quality, stale or conflicting evidence must not be silently converted into a known label.
3. Evaluate false-positive rates on representative non-target scenes before any operational trial.
4. No foundation model controls actuators directly; navigation remains behind a deterministic safety supervisor.
5. Run dependency/license checks and generate an SBOM for each release.
6. Keep test data access-controlled and minimize retained imagery and unrelated personal data.

## Required report fields

Include `schema_version`, `project`, `run_id`, timezone-aware `run_date_utc`, `dataset{name,version,split}`, `model{name,version}`, `hardware{platform}`, `software{os,python}`, `config{seed}` and numeric `metrics`. Include metric definitions, class prevalence and trial counts in the report narrative.
