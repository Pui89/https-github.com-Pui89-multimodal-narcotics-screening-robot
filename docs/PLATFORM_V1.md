# Platform v1.0 maturity

## Runtime
- Monitoring for latency, dropped frames, queue depth, resources, sensor health, sync drift, OOD, abstention and safety-gate events.
- Bounded temporal evidence accumulation.
- Covariance-aware 3D evidence quality.
- Explicit human review decisions.
- Model lifecycle governance.
- Reproducible experiment metadata.
- Standard robustness stress scenarios.

## Service boundary
The framework-neutral service maps cleanly to POST /screen, GET /health, GET /metrics, GET /models, GET /events/{id}, and POST /review. It must never expose unrestricted actuator commands.

## Safety architecture
Perception/reasoning: Sensors → Perception → Evidence → Reasoning → Human Review.
Navigation: LiDAR/Depth/IMU → SLAM → Planner → Deterministic Safety Gate → ROS 2.

Foundation models remain advisory.

## Release security
Tagged releases build Python artifacts, generate an SBOM, and create signed GitHub artifact attestations. Attestations provide provenance/integrity metadata; consumers must verify them before relying on them as a security control.

Physical deployment remains conditional on independent validation, calibration, robustness testing, cybersecurity review, human-review procedures and deterministic safety testing.
