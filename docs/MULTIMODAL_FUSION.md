# Multimodal Fusion Research Method

## Proposed formulation

Let each modality produce a representation:

$$z = F(z_{RGB}, z_{Thermal/NIR}, z_{Depth}, z_{LiDAR}, z_{Temporal})$$

The proposed system estimates both a prediction distribution $p(y|x)$ and uncertainty $U$.

A practical adaptive fusion formulation is:

$$z_f = \sum_m w_m z_m, \qquad w_m \ge 0, \quad \sum_m w_m = 1$$

where weights $w_m$ depend on sensor quality, missing modalities, learned reliability, and validation-time calibration.

## Research comparison

Compare:

- early concatenation
- late probability fusion
- attention-based fusion
- reliability-weighted adaptive fusion
- adaptive fusion + uncertainty/OOD

The contribution is only defensible if adaptive fusion improves robustness on held-out stress conditions.

## Missing-modality protocol

During training and evaluation, explicitly simulate missing or corrupted modalities. The model must not silently treat unavailable evidence as reliable evidence.

## Temporal extension

For sequential observations:

$$h_t = T(z_{f,t-k:t})$$

Evaluate whether temporal context improves robustness while preserving an acceptable latency budget.

## Evidence provenance

Every prediction should retain modality availability, sensor timestamps, model version, preprocessing version, and quality-gate status.

## Chemical-identification boundary

Visual, thermal, depth, LiDAR and foundation-model evidence are screening signals. They are not a substitute for validated chemical analysis.
