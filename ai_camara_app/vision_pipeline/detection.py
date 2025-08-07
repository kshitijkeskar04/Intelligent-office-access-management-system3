from typing import List, Tuple

import cv2
import numpy as np
from ultralytics import YOLO


class PersonDetector:
    """Wrapper around YOLOv8 to detect people in an image.

    The model returns bounding boxes (x1, y1, x2, y2) and confidence scores
    filtered to the person class (class id 0 in COCO).
    """

    def __init__(self, model_path: str = "yolov8n.pt", device: str = "cpu") -> None:
        self.model = YOLO(model_path)
        self.device = device

    def detect(self, frame: np.ndarray, conf_thres: float = 0.3) -> List[Tuple[int, int, int, int, float]]:
        """Detect persons in a frame.

        Args:
            frame: BGR image as numpy array (OpenCV format)
            conf_thres: discard detections below this confidence

        Returns:
            List of tuples (x1, y1, x2, y2, confidence)
        """
        # Resize to model default; YOLO auto-handles sizes
        results = self.model(frame, verbose=False, device=self.device)[0]
        boxes: List[Tuple[int, int, int, int, float]] = []
        for xyxy, cls, conf in zip(results.boxes.xyxy, results.boxes.cls, results.boxes.conf):
            if int(cls) == 0 and float(conf) >= conf_thres:  # person class
                x1, y1, x2, y2 = [int(x) for x in xyxy]
                boxes.append((x1, y1, x2, y2, float(conf)))
        return boxes
