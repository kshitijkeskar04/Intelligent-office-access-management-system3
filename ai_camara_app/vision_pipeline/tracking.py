from typing import List, Tuple

import numpy as np
from deep_sort_realtime.deepsort_tracker import DeepSort


class Tracker:
    """DeepSORT tracker wrapper for maintaining consistent IDs across frames."""

    def __init__(self, max_age: int = 30):
        # Initialize DeepSort with reasonable defaults for person tracking
        self.deepsort = DeepSort(max_age=max_age)

    def update(
        self, boxes: List[Tuple[int, int, int, int, float]], frame: np.ndarray
    ) -> List[Tuple[int, int, int, int, int]]:
        """Update tracker with detections.

        Args:
            boxes: list of (x1, y1, x2, y2, conf)
            frame: original BGR frame for appearance features

        Returns:
            List of (track_id, x1, y1, x2, y2)
        """
        if not boxes:
            boxes = np.empty((0, 5))
        boxes_np = np.array(boxes)
        tracks = self.deepsort.update_tracks(boxes_np, frame=frame)
        results = []
        for t in tracks:
            if not t.is_confirmed():
                continue
            track_id = t.track_id
            l, t_, r, b = map(int, t.to_ltrb())
            results.append((track_id, l, t_, r, b))
        return results
