# AI Robot Layer

This layer turns the screening platform into a simulation-ready mobile AI robot architecture. It is designed for **non-invasive observation of accessible objects/environments**, not internal-body searching or autonomous enforcement.

## Robot stack

Sensors -> perception -> 3D world model -> mission planner -> Nav2 -> deterministic safety gate -> ROS2 hardware interface.

Recommended hardware targets:
- Jetson Orin Nano for AI perception
- Raspberry Pi 5 for auxiliary telemetry/safety services
- RGB-D camera
- optional thermal/NIR camera
- 2D/3D LiDAR
- IMU
- differential-drive base
- independent physical E-stop

The robot should stop when localization confidence, obstacle clearance, human exclusion, watchdog, battery or E-stop checks fail.
