from camera_utils import CameraStream
from face_utils import FaceRecognizer
from database.es_connector import ESClient
import time

class AccessSystem:
    def __init__(self):
        self.camera = CameraStream()
        self.recognizer = FaceRecognizer()
        self.db = ESClient()
        self.running = False
        
    def start(self):
        self.running = True
        print("Access system started")
        while self.running:
            self.process_frame()
            time.sleep(0.1)
            
    def process_frame(self):
        frame = self.camera.get_frame()
        if frame is not None:
            faces = self.recognizer.detect_faces(frame)
            for face in faces:
                emp_id, confidence = self.recognizer.identify(face)
                if confidence > 0.7:  # Threshold
                    self.db.log_access(
                        employee_id=emp_id,
                        confidence=confidence,
                        status="granted"
                    )
                else:
                    self.db.log_access(
                        employee_id="unknown",
                        confidence=confidence,
                        status="denied"
                    )

if __name__ == "__main__":
    system = AccessSystem()
    system.start()