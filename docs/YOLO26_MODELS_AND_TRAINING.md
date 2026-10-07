# YOLO26 Models & Training — Multimodal Narcotics Screening Robot

Ultralytics YOLO26 is integrated as a **visual proposal layer** for defensive, non-invasive screening of accessible external objects/environments. It can propose visual candidates for human review; it does **not** prove chemical identity and never directly controls actuators.

## Model matrix

| Model | Filenames | Task | Training | Validation | Inference | Export |
|---|---|---|---|---|---|---|
| YOLO26 | `yolo26n.pt` · `yolo26s.pt` · `yolo26m.pt` · `yolo26l.pt` · `yolo26x.pt` | Detection | ✅ | ✅ | ✅ | ✅ |
| YOLO26-seg | `yolo26n-seg.pt` … `yolo26x-seg.pt` | Instance Segmentation | ✅ | ✅ | ✅ | ✅ |
| YOLO26-sem | `yolo26n-sem.pt` … `yolo26x-sem.pt` | Semantic Segmentation | ✅ | ✅ | ✅ | ✅ |
| YOLO26-depth | `yolo26n-depth.pt` … `yolo26x-depth.pt` | Depth Estimation | ✅ | ✅ | ✅ | ✅ |
| YOLO26-cls | `yolo26n-cls.pt` … `yolo26x-cls.pt` | Classification | ✅ | ✅ | ✅ | ✅ |
| YOLO26-pose | `yolo26n-pose.pt` … `yolo26x-pose.pt` | Pose / Keypoints | ✅ | ✅ | ✅ | ✅ |
| YOLO26-obb | `yolo26n-obb.pt` … `yolo26x-obb.pt` | Oriented Detection | ✅ | ✅ | ✅ | ✅ |

YOLO26 also provides architecture-only `yolo26-p2.yaml` and `yolo26-p6.yaml` configurations for small/large-object variants. Official documentation lists all seven task families with train, validation, inference, and export support. See the official docs: https://docs.ultralytics.com/models/yolo26

## Recommended screening classes

Use neutral, evidence-oriented labels in training data:

```yaml
path: data/screening_yolo26
train: images/train
val: images/val

names:
  0: accessible_object
  1: packaging_like_object
  2: powder_like_material
  3: crystal_like_material
  4: tablet_like_object
  5: unknown_substance
  6: environmental_debris
```

These are visual categories, **not chemical-identification labels**. Do not train the robot to assert that an image proves heroin, amphetamine, methamphetamine, or another chemical identity.

## Install

```bash
python -m pip install -U ultralytics huggingface-hub
```

## Training

```bash
yolo detect train \
  model=yolo26n.pt \
  data=data/screening_yolo26.yaml \
  epochs=100 \
  imgsz=640 \
  batch=16
```

Python:

```python
from ultralytics import YOLO

model = YOLO("yolo26n.pt")
results = model.train(
    data="data/screening_yolo26.yaml",
    epochs=100,
    imgsz=640,
    batch=16,
)
```

For deployment, compare `n/s/m/l/x` using measured latency, memory, false-positive rate, and review workload rather than assuming the largest model is best.

## Validation

```bash
yolo detect val \
  model=runs/detect/train/weights/best.pt \
  data=data/screening_yolo26.yaml \
  imgsz=640
```

Track mAP50, mAP50-95, precision, recall, per-class confusion, false positives, false negatives, latency, memory, and unknown/OOD behavior. Evaluate difficult lighting, occlusion, clutter, reflections, camera motion, distance, and partial visibility.

## Inference

```bash
yolo detect predict \
  model=runs/detect/train/weights/best.pt \
  source=data/screening_scenes \
  imgsz=640
```

YOLO26 also supports an optional NMS-free one-to-one inference head:

```bash
yolo detect predict \
  model=runs/detect/train/weights/best.pt \
  source=data/screening_scenes \
  nms=False
```

The default one-to-many path is useful when prioritizing accuracy; measure the NMS-free path before selecting it for a specific embedded deployment.

## Export

ONNX:

```bash
yolo export model=runs/detect/train/weights/best.pt format=onnx
```

TensorRT:

```bash
yolo export model=runs/detect/train/weights/best.pt format=engine
```

Ultralytics documents ONNX, TensorRT, OpenVINO, TorchScript, CoreML and additional export targets. Always validate the exported model against the original checkpoint on the project's own validation set.

## Robot integration

```text
RGB / RGB-D / Thermal / NIR / LiDAR
                 |
                 v
             YOLO26
                 |
       visual candidate proposals
                 |
                 v
     3D evidence + tracking + OOD
                 |
                 v
     multimodal review assistance
                 |
                 v
        HUMAN REVIEW GATE
                 |
                 v
       audit / evidence record

Navigation is separate:
LiDAR + Depth + IMU -> SLAM -> Planner
                              |
                              v
                    Deterministic Safety Gate
                              |
                              v
                         ROS 2 Controller
```

YOLO26 output is never an autonomous enforcement decision. Foundation models and perception models never directly command motors, restraint mechanisms, seizure mechanisms, or other actuators.

## Safety and evidence rules

- Visual predictions are screening hypotheses only.
- Preserve `unknown_substance` when evidence is insufficient.
- Do not infer ingestion or internal-body presence.
- Do not identify people by demographic or unrelated attributes.
- Keep screening and navigation pipelines separated.
- Require human review for consequential cases.
- Store provenance: sensor, timestamp, model/checkpoint, preprocessing, calibration, and reviewer decision.
- Use deterministic emergency-stop, workspace, collision, velocity, and actuator interlock controls.

## Official references

- Hugging Face model repository: https://huggingface.co/Ultralytics/YOLO26
- Ultralytics YOLO26 documentation: https://docs.ultralytics.com/models/yolo26
- Ultralytics export documentation: https://docs.ultralytics.com/modes/export
