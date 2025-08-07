from typing import Optional

import numpy as np
import cv2
import torch
import numpy as np
from facenet_pytorch import InceptionResnetV1, MTCNN

# Load MTCNN for face cropping and Facenet model once at module import
_device = "cuda" if torch.cuda.is_available() else "cpu"
_mtcnn = MTCNN(image_size=160, device=_device)
_resnet = InceptionResnetV1(pretrained="vggface2").eval().to(_device)


def extract_face_embedding(image: np.ndarray) -> Optional[np.ndarray]:
    """Generate a 512-D face embedding using FaceNet (PyTorch).

    Args:
        image: BGR frame (numpy array)
    Returns:
        1-D numpy array (512 floats) if a face is found, otherwise None.
    """
    # Convert to RGB and get face crop via MTCNN
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    face = _mtcnn(rgb)
    if face is None:
        return None

    with torch.no_grad():
        embedding = _resnet(face.unsqueeze(0).to(_device))
    return embedding.squeeze(0).cpu().numpy().astype(np.float32)
