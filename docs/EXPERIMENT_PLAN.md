# PhD-Level Experimental Plan

## 1. Experimental objective

Evaluate whether multimodal, uncertainty-aware, open-set screening is more robust and better calibrated than single-modality and naive-fusion alternatives.

## 2. Baselines

Run identical train/validation/test protocols for:

1. RGB only
2. Thermal/NIR only
3. Depth only
4. LiDAR only
5. RGB + depth
6. RGB + thermal/NIR
7. RGB + thermal/NIR + depth
8. Full multimodal baseline
9. Proposed adaptive fusion + uncertainty + open-set method

No result should be claimed until the corresponding experiment is actually executed.

## 3. Stress conditions

Create controlled evaluation splits for:

- low illumination
- motion blur
- partial occlusion
- distance variation
- viewpoint variation
- clutter/background shift
- sensor dropout
- sensor corruption/noise
- cross-environment domain shift
- previously unseen objects/classes

Use authorized external-object data and synthetic/simulation augmentation where real data are unavailable.

## 4. Metrics

### Screening

- precision, recall, F1
- macro-F1
- balanced accuracy
- AUROC
- AUPRC

### Open-set recognition

- unknown detection rate
- AUROC for known-vs-unknown
- FPR@95TPR
- OSCR

### Uncertainty/calibration

- Expected Calibration Error (ECE)
- Brier score
- reliability diagrams
- risk-coverage curves
- selective risk

### Robotics

- end-to-end latency
- localization error
- navigation success
- collision/near-collision rate
- trajectory deviation
- safe-stop response latency

### Human review

- reviewer agreement
- review time
- false-alarm reduction
- abstention acceptance rate

## 5. Ablation matrix

Ablate one component at a time:

- remove thermal/NIR
- remove depth
- remove LiDAR
- remove temporal representation
- remove OOD detector
- remove calibration
- remove abstention
- replace adaptive fusion with concatenation

## 6. Statistical protocol

Use fixed seeds, documented splits, confidence intervals, and paired comparisons where appropriate. Report mean ± variation across repeated runs. Avoid cherry-picking a favorable seed.

## 7. Reproducibility rule

Every reported number must map to a versioned configuration, dataset split, model checkpoint, code revision, and evaluation command.
