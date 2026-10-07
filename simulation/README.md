# Robotics Simulation Boundary

Simulation is the default integration layer before physical hardware.

## Boundary

```
Sensors -> Perception -> Evidence -> Reasoning -> Human Review
                                  |
LiDAR/Depth/IMU -> SLAM -> Planner -> Deterministic Safety Gate -> ROS 2
```

Foundation models are advisory only. This directory must not provide a direct model-to-motor path.

## Dry-run contract

A navigation intent may contain:
- target frame
- requested direction
- speed limit
- timestamp
- reason
- safety state

The dry-run adapter records intent without sending actuator commands. Physical integration requires an independently validated ROS 2 safety controller and emergency-stop path.
