import face_recognition
import numpy as np
import os

class FaceRecognizer:
    def __init__(self):
        self.known_encodings = []
        self.known_ids = []
        self.load_known_faces()
        
    def load_known_faces(self):
        for filename in os.listdir("../data/employees"):
            if filename.endswith(".jpg"):
                image = face_recognition.load_image_file(f"../data/employees/{filename}")
                encodings = face_recognition.face_encodings(image)
                if encodings:
                    self.known_encodings.append(encodings[0])
                    self.known_ids.append(filename.split(".")[0])
    
    def detect_faces(self, frame):
        rgb_frame = frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        return list(zip(face_locations, face_encodings))
        
    def identify(self, face_data):
        face_encoding = face_data[1]
        matches = face_recognition.compare_faces(self.known_encodings, face_encoding)
        face_distances = face_recognition.face_distance(self.known_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        
        if matches[best_match_index]:
            return self.known_ids[best_match_index], 1 - face_distances[best_match_index]
        return "unknown", 0