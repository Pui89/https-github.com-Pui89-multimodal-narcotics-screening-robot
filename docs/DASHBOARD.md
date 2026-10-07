# Evaluation Dashboard

The dashboard contract is model-agnostic and must remain separated from actuator authority.

Panels:
- sensor health and synchronization
- RGB/depth/thermal/LiDAR evidence
- 3D evidence map
- screening hypothesis and confidence
- OOD and abstention state
- cross-modal agreement
- event timeline
- evidence provenance
- human-review queue
- safety state and emergency-stop status
- evaluation metrics and latency

Allowed actions are review, reprocess and stop. Unrestricted LLM-to-motor commands are prohibited.
