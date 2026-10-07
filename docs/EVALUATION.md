# Evaluation and Validation

The project separates model performance from system trustworthiness.

Evaluation layers:
1. Perception: detection, segmentation, tracking.
2. Fusion: cross-modal agreement and degradation behavior.
3. Open-set: unknown rejection and abstention.
4. Calibration: confidence versus empirical correctness.
5. Robustness: blur, low light, glare, occlusion, sensor dropout and domain shift.
6. Systems: latency, memory, throughput and synchronization.
7. Safety: deterministic gate invariants and zero unauthorized actuator paths.
8. Human review: reviewer agreement and audit completeness when lawfully collected.

Reporting rule: never insert placeholder benchmark values. Every reported value must identify dataset/version, model version, hardware, configuration and run date.

Scenario matrix: normal, low light, missing thermal, missing depth, unknown object, sensor disagreement, and fully degraded perception.

The platform screens accessible external objects/environments only; it does not diagnose internal-body ingestion or establish chemical identity.
