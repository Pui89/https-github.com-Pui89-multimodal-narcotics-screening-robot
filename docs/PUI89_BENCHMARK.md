# PUI89 Benchmark

## Benchmark principles
- measured results only;
- versioned datasets and models;
- held-out evaluation;
- explicit UNKNOWN/OOD testing;
- evidence provenance;
- safety metrics separate from classification metrics.

| Area | Metrics |
|---|---|
| Perception | precision, recall, F1 |
| Multimodal fusion | agreement, contradiction detection |
| Unknown handling | AUROC/AUPR, abstention precision, selective risk |
| Calibration | ECE, Brier score |
| Evidence | provenance completeness, hash verification |
| Operations | inspection throughput, latency, uptime |
| Governance | review routing, audit completeness, unsafe-action rejection |

## Scenarios
Normal, low light, occlusion, blur, sensor dropout, calibration error, conflicting modalities, OOD objects, network loss, low battery, unexpected geometry and operator review.

## Record
experiment_id, dataset_version, hardware, sensor_configuration, model_version, software_commit, scenario, metrics, confidence, uncertainty, OOD_score, failures, safety_events, review_outcome and limitations.
