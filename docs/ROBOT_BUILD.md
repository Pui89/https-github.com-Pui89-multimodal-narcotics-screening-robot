# AI Robot Build Plan

## Phase 1 — simulation

1. Load the URDF into ROS2/Gazebo or Isaac Sim.
2. Add RGB-D, LiDAR and IMU sensor plugins.
3. Run SLAM and Nav2.
4. Connect the screening pipeline as an observation service.
5. Add the deterministic safety gate.

## Phase 2 — edge AI

Run YOLO/SAM3-style perception and multimodal reasoning on Jetson-class hardware. Fuse RGB-D/LiDAR observations into a 3D scene representation.

## Phase 3 — physical robot

Use a differential-drive mobile base with an independent E-stop, watchdog and hardware safety controller. The AI layer may request safe navigation goals but cannot bypass the safety controller.

## Phase 4 — validation

Test localization, obstacle avoidance, sensor failures, false positives/negatives, unknown objects, human entry into exclusion zones, communications loss and emergency stop.

## Important boundary

The robot is an observation/screening platform for accessible external objects and environments. It is not an autonomous police, medical or invasive-search robot and cannot determine whether a person has swallowed or concealed narcotics inside their body.
