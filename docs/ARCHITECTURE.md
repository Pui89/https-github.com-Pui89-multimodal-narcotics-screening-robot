# Architecture

Perception: RGB/RGB-D/thermal/NIR/LiDAR -> YOLO-family detection -> SAM3-style masks -> tracking -> depth/LiDAR 3D evidence -> open-set anomaly detection.

Reasoning: Qwen3-VL and Gemma4-E4B-it can provide independent review aids; V-JEPA2-style temporal representations can add video context. Outputs remain hypotheses with uncertainty.

Navigation: LiDAR/depth/IMU SLAM -> local map -> Nav2/planner -> optional MPC -> deterministic safety gate -> ROS2 controller.

Edge/cloud: Jetson Orin Nano or Raspberry Pi 5 can handle edge preprocessing and telemetry. MQTT/WebSockets may transport authorized telemetry/video. Emergency stop must remain local.

Simulation: Isaac Sim/Isaac Lab and LeRobot support simulation and policy evaluation. Synthetic data does not establish real-world chemical detection performance.
