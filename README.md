# Multimodal Narcotics Screening Robot

Defensive, non-invasive AI platform for screening accessible external objects and environments for anomalous substances and suspected narcotics-related visual patterns, with multimodal evidence fusion, uncertainty handling, human review, and safe robotics integration.

SAFETY: ordinary cameras, thermal/NIR, depth, LiDAR, and AI models cannot reliably identify a drug hidden inside a person's organs or determine whether someone has ingested a substance. This project does not perform internal-body diagnosis, medical examination, forensic chemical identification, restraint, seizure, or autonomous enforcement. Suspected ingestion/internal-body cases require qualified medical/forensic professionals using validated procedures.

## Stack

- RGB/RGB-D/thermal/NIR/LiDAR perception
- YOLO-family detection, SAM3-style segmentation, tracking
- 3D localization and evidence geometry
- open-set anomaly and unknown handling
- Qwen3-VL and Gemma4-E4B-it as review aids
- V-JEPA2-style temporal representation
- ROS2/Nav2, LiDAR/depth/IMU SLAM, optional MPC
- MQTT/WebSockets telemetry
- Isaac Sim/Isaac Lab and LeRobot simulation hooks
- deterministic safety gate before robot motion

## Screening taxonomy

amphetamine, heroin, methamphetamine_crystal, narcotic_unknown, unknown_substance

Predictions are screening hypotheses only, never proof of chemical identity. Unknown and unseen observations remain unknown.

## Architecture

RGB/RGB-D/Thermal/NIR/LiDAR -> detection/segmentation/tracking -> 3D evidence fusion -> anomaly/unknown screening -> multimodal reasoning -> uncertainty calibration -> HUMAN REVIEW -> audit/evidence record.

Navigation is separate: LiDAR/Depth/IMU -> SLAM/local map -> Nav2/planner/MPC -> deterministic safety gate -> ROS2 controller. Foundation models never directly command motors.

## Quick start

python -m pip install -e '.[dev]'
pytest -q

## Ethics

Use only lawful, authorized and proportionate screening. Minimize retained imagery, protect evidence access, log reviewer decisions, and avoid demographic or unrelated person identification.

## 3D / 4D Robot Concept

![3D/4D concept](docs/multimodal_narcotics_screening_robot_3d_4d_concept.svg)

Realistic concept visualization of the mobile screening robot, sensor mast, screening target, multimodal sensor fusion and time-indexed 4D trajectory. The visualization is a design concept, not a claim of chemical identification capability.

- [3D/4D concept image](docs/multimodal_narcotics_screening_robot_3d_4d_concept.svg)
- [3D/4D video preview](docs/multimodal_narcotics_screening_robot_3d4d_preview.mp4)

## Pipeline Overview

**Sense → Quality Gate → Perceive → Track → 3D Evidence Fusion → Anomaly/Unknown Screening → Multimodal Reasoning → Uncertainty Calibration → Human Review → Audit → Safe Robot Navigation**

See [Pipeline Overview](docs/PIPELINE_OVERVIEW.md) for the full safety-first workflow and [AI Architecture](docs/AI_ARCHITECTURE.md) for the multimodal system diagram.

> Safety note: screening outputs are hypotheses for authorized human review. They are not proof of chemical identity, and foundation models do not directly control robot motors.
