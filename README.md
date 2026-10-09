# Multimodal Narcotics Screening Robot


## PUI89 AI Robotics Platform

**Multimodal AI security and inspection platform with evidence-aware screening, uncertainty and human review.**

This repository is one vertical implementation of the **PUI89 AI Robotics** platform for security / inspection. The common architecture is:

```text
Multimodal Sensors
      ↓
Quality / Health Gate
      ↓
Perception + Tracking
      ↓
3D / 4D World Model
      ↓
Uncertainty + OOD
      ↓
Foundation-Model Reasoning
      ↓
Task Planning
      ↓
Deterministic Safety Supervisor
      ↓
ROS 2 / Robot Control
      ↓
Telemetry / Evidence
      ↓
MLOps / Fleet Learning
```

### Executable end-to-end screening reference

- [E2E screening workflow: run instructions, privacy and safety boundaries, benchmark plan](docs/E2E_SCREENING_WORKFLOW.md)
- [Synthetic object/container case](examples/synthetic_screening_case.json)
- [Runnable evidence-fusion workflow](e2e_screening/workflow.py)
- [Automated tests](tests/test_e2e_screening.py)
- [Python 3.10–3.12 CI workflow](.github/workflows/e2e-screening.yml)

This software reference validates external modality scores, applies quality/OOD gates, fuses accepted evidence, and creates a review-queue result. It explicitly rejects person screening and does not confirm substance presence or authorize enforcement. It is not a trained or validated detector; real deployments require lawful data governance, confirmatory testing protocols, independent validation, and human oversight.

### Product tiers

- **PUI89 Research** — universities, robotics competitions, researchers
- **PUI89 Professional** — industrial customers, logistics, ports, infrastructure, authorized security operators
- **PUI89 Enterprise** — large corporations, governments, logistics, ports, infrastructure

### Cross-environment research

The same perception/world-model/uncertainty/safety interfaces are designed to transfer between agriculture, disaster response and security/inspection. Transfer must be measured with the repository benchmark; it is not assumed from architecture alone.

- [Optional DINOv2 + Anomalib integration, end-to-end verification and tests](docs/OPEN_SOURCE_VISION_INTEGRATION.md)

### Evidence standard

This project separates **targets, prototypes and measured results**. Production or field-validation claims require reproducible benchmark evidence, failure testing, and documented safety validation.

See:
- [PUI89 Benchmark](docs/PUI89_BENCHMARK.md)
- [Cross-Environment Transfer Benchmark](docs/PUI89_TRANSFER_BENCHMARK.md)
- [Product Tiers](docs/PUI89_PRODUCT_TIERS.md)
- [Failure and UNKNOWN Protocol](docs/PUI89_FAILURE_AND_UNKNOWN_PROTOCOL.md)
- [MLOps Model Lifecycle](docs/PUI89_MLOPS_MODEL_LIFECYCLE.md)
- [Research, Competition and Commercial Evidence](docs/PUI89_RESEARCH_COMPETITION_INVESTOR.md)
- [12-Month Roadmap](docs/PUI89_12_MONTH_ROADMAP.md)

Defensive, non-invasive AI platform for screening accessible external objects and environments for anomalous substances and suspected narcotics-related visual patterns, with multimodal evidence fusion, uncertainty handling, human review, and safe robotics integration.

SAFETY: ordinary cameras, thermal/NIR, depth, LiDAR, and AI models cannot reliably identify a drug hidden inside a person's organs or determine whether someone has ingested a substance. This repository's new reference workflow is restricted to object/container cases and never emits an automated enforcement decision.
