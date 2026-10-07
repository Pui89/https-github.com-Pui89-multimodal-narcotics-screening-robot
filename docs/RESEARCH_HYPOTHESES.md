# Research Hypotheses

## Proposed PhD research theme

**Uncertainty-Aware Multimodal Robotic Screening and Open-Set Anomaly Detection**

### Central research question

Can uncertainty-aware multimodal sensor fusion improve screening robustness under sensor degradation, environmental domain shift, and previously unseen observations compared with single-modality and naive-fusion baselines?

## Testable hypotheses

- **H1 — Multimodal robustness:** RGB + thermal/NIR + depth/LiDAR evidence improves macro-F1 and balanced accuracy over the strongest single-modality baseline under controlled domain shift.
- **H2 — Adaptive fusion:** confidence-aware/adaptive fusion degrades more gracefully than fixed concatenation when one or more sensors are corrupted or unavailable.
- **H3 — Open-set safety:** explicit unknown/OOD handling reduces false acceptance of unseen objects compared with a closed-set classifier.
- **H4 — Calibration:** calibrated uncertainty and abstention improve selective risk at a fixed coverage level.
- **H5 — Temporal evidence:** temporal aggregation improves robustness to blur, partial occlusion, and intermittent sensor dropout without unacceptable latency.
- **H6 — Safety separation:** keeping foundation-model reasoning outside the actuator-control path provides a verifiable safety boundary without preventing useful multimodal evidence summarization.

## Scientific claim boundary

This project studies **screening hypotheses from accessible external observations**, not chemical proof, medical diagnosis, internal-body detection, or autonomous enforcement. Any consequential conclusion requires qualified human review and, where applicable, validated laboratory/forensic procedures.

## What would falsify the thesis

The proposed method should not be presented as superior if repeated controlled experiments show no statistically meaningful improvement over strong baselines, or if gains disappear under realistic domain shift and sensor failure.

## Target research contribution

A reproducible benchmark, uncertainty-aware multimodal fusion method, open-set/abstention protocol, safety-constrained robotic integration, and statistically defensible evaluation package.
