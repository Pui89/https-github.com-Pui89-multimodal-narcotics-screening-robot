# Digital twin integration

Use simulation before physical robot connection:

Synthetic RGB/Depth/Thermal/LiDAR/IMU → Perception → Evidence Graph → Screening → Review → Planner → Deterministic Safety Gate.

Reuse the same event schemas, model registry, evaluation runner and safety boundaries for simulation and hardware-in-the-loop testing. Stress-test missing sensors, clock skew, blur, lighting changes, LiDAR sparsity, depth corruption, contradictory modalities and OOD observations.
