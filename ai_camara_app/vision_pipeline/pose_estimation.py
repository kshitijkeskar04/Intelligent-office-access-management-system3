from typing import Optional

import cv2
import numpy as np

try:
    import mediapipe as mp  # Optional; will not be available in lightweight install
    mp_pose = mp.solutions.pose
except ModuleNotFoundError:
    mp = None
    mp_pose = None


POSE_EMBEDDING_SIZE = 32  # We will downsample to 32 dims for storage


def _flatten_landmarks(landmarks) -> np.ndarray:
    coords = []
    for lm in landmarks:
        coords.extend((lm.x, lm.y, lm.z))
    return np.array(coords, dtype=np.float32)


def get_body_embedding(frame: np.ndarray) -> Optional[np.ndarray]:
    """Return a fixed-length representation of body dimensions.

    Uses MediaPipe Pose to extract landmarks and returns the first 32 values of the
    flattened coordinate array (zero-padded if fewer).
    """
    if mp_pose is None:
        return None
    with mp_pose.Pose(static_image_mode=True) as pose:
        results = pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        if not results.pose_landmarks:
            return None
        vec = _flatten_landmarks(results.pose_landmarks.landmark)
        # Pad or truncate to target dimension
        if vec.size >= POSE_EMBEDDING_SIZE:
            return vec[:POSE_EMBEDDING_SIZE]
        padded = np.zeros((POSE_EMBEDDING_SIZE,), dtype=np.float32)
        padded[: vec.size] = vec
        return padded
