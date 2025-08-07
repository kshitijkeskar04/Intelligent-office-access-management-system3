import cv2

class CameraStream:
    def __init__(self, camera_id=0):
        self.camera_id = camera_id
        self.cap = cv2.VideoCapture(camera_id)
        
    def get_frame(self):
        ret, frame = self.cap.read()
        if ret:
            return frame
        return None
        
    def release(self):
        self.cap.release()