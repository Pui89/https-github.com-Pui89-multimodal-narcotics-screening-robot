"""YOLO26 visual-proposal adapter for defensive screening.

This module intentionally stops at perception proposals. It does not identify
chemical composition and does not expose actuator-control methods.
"""

from dataclasses import dataclass
from typing import Any

import numpy as np


@dataclass
class YOLO26Proposal:
    class_id: int
    class_name: str
    confidence: float
    xyxy: tuple[float, float, float, float]


class YOLO26ScreeningDetector:
    """Run YOLO26 as a visual candidate-proposal layer."""

    def __init__(
        self,
        weights: str = "yolo26n.pt",
        confidence: float = 0.35,
        imgsz: int = 640,
    ) -> None:
        try:
            from ultralytics import YOLO
        except ImportError as exc:
            raise RuntimeError(
                "Install YOLO26 dependencies with: "
                "python -m pip install ultralytics huggingface-hub"
            ) from exc

        self.model = YOLO(weights)
        self.confidence = confidence
        self.imgsz = imgsz

    @staticmethod
    def _uint8_rgb(image: Any) -> np.ndarray:
        arr = np.asarray(image)
        if arr.ndim != 3 or arr.shape[2] != 3:
            raise ValueError("Expected an RGB image with shape HxWx3.")
        if arr.dtype != np.uint8:
            arr = np.clip(arr, 0, 255).astype(np.uint8)
        return arr

    def predict(self, rgb_image: Any, *, nms: bool = True) -> list[YOLO26Proposal]:
        """Return visual proposals only; no chemical-identification decision."""
        image = self._uint8_rgb(rgb_image)
        results = self.model.predict(
            source=image,
            conf=self.confidence,
            imgsz=self.imgsz,
            nms=nms,
            verbose=False,
        )

        proposals: list[YOLO26Proposal] = []
        for result in results:
            names = result.names
            boxes = getattr(result, "boxes", None)
            if boxes is None:
                continue

            for box in boxes:
                cls = int(box.cls.item())
                confidence = float(box.conf.item())
                xyxy = tuple(float(v) for v in box.xyxy[0].tolist())
                proposals.append(
                    YOLO26Proposal(
                        class_id=cls,
                        class_name=str(names[cls]),
                        confidence=confidence,
                        xyxy=xyxy,
                    )
                )

        return proposals
