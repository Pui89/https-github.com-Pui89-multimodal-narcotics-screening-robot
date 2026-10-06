# Robotics integration

The perception and reasoning layer is separated from robot control. ROS2 topics/services can carry observations and authorized navigation requests. Nav2 handles route orchestration; LiDAR/depth/IMU SLAM supports GPS-denied localization; an optional MPC layer can track validated trajectories.

Foundation models and generative policies have no direct motor authority. Every motion request must pass deterministic emergency-stop, localization, collision, human-exclusion, workspace, speed/force, actuator and watchdog checks.

The platform does not authorize manipulation of people, invasive searches or cutting into a person.
