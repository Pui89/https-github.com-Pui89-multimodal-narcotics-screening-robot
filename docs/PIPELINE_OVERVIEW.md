# Pipeline Overview — Multimodal Narcotics Screening Robot

## Safety-first mission

The platform is designed for authorized, non-invasive screening of accessible external objects and environments. It produces screening hypotheses and evidence for trained human review; it does not perform internal-body diagnosis, chemical identification, restraint, seizure, or autonomous enforcement.

## End-to-end pipeline

**Sense → Quality Gate → Perceive → Track → 3D Evidence Fusion → Anomaly/Unknown Screening → Multimodal Reasoning → Uncertainty Calibration → Human Review → Audit → Safe Robot Navigation**

1. **Sense** — RGB/RGB-D, thermal/NIR, LiDAR, IMU and environmental telemetry acquire synchronized observations.
2. **Quality Gate** — reject blurred, saturated, occluded, stale or low-quality observations.
3. **Perceive** — detection, segmentation and tracking identify relevant accessible objects, surfaces, containers and context.
4. **Track** — temporal association maintains target identity and confidence without unnecessary person identification.
5. **3D Evidence Fusion** — depth/LiDAR geometry aligns observations into a spatial evidence map with sensor provenance.
6. **Anomaly / Unknown Screening** — preserve an explicit unknown state for unseen or ambiguous evidence.
7. **Multimodal Reasoning** — vision-language models summarize evidence and propose review explanations; advisory only.
8. **Uncertainty Calibration** — combine confidence, disagreement, missing modalities and out-of-distribution signals.
9. **Human Review** — trained operator reviews evidence, uncertainty and rationale before a conclusion is recorded.
10. **Audit / Evidence Record** — store minimal necessary metadata, timestamps, sensor provenance, model versions and reviewer decisions.
11. **Safe Robot Navigation** — SLAM → planner → deterministic safety gate → ROS 2 controller. Foundation models never directly command motors.

## 4D concept

The 4D layer adds time to the spatial evidence map, visualizing target motion, robot trajectory, changing sensor confidence and predicted obstacle states. Time prediction remains subordinate to deterministic safety constraints.

## Screening taxonomy

- `amphetamine`
- `heroin`
- `methamphetamine_crystal`
- `narcotic_unknown`
- `unknown_substance`

These labels are screening hypotheses only, not proof of chemical identity. Confirmatory laboratory/forensic procedures remain authoritative.

## Governance

- Authorized use only.
- Minimize retained imagery.
- Avoid unrelated demographic/person identification.
- Preserve unknown and abstain outcomes.
- Require human review for consequential decisions.
- Log model/version and reviewer provenance.
- Keep safety controls independent from foundation-model reasoning.
