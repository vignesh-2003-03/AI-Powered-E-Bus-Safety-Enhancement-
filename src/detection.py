# detection.py
import numpy as np
import cv2
import dlib
import imutils
from imutils import face_utils

CASCADE_PATH = "haarcascade_frontalface_default.xml"
PREDICTOR_PATH = "shape_predictor_68_face_landmarks.dat"

def euclidean_dist(ptA, ptB):
    return np.linalg.norm(ptA - ptB)

def eye_aspect_ratio(eye):
    A = euclidean_dist(eye[1], eye[5])
    B = euclidean_dist(eye[2], eye[4])
    C = euclidean_dist(eye[0], eye[3])
    return (A + B) / (2.0 * C)

class EyeDetector:
    def __init__(self):
        print("[INFO] Loading predictor...")
        self.detector = cv2.CascadeClassifier(cv2.data.haarcascades + CASCADE_PATH)
        self.predictor = dlib.shape_predictor(PREDICTOR_PATH)
        (self.left_start, self.left_end) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
        (self.right_start, self.right_end) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

    def detect_eyes(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rects = self.detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5,
                                               minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

        for (x, y, w, h) in rects:
            rect = dlib.rectangle(int(x), int(y), int(x + w), int(y + h))
            shape = self.predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)

            left_eye = shape[self.left_start:self.left_end]
            right_eye = shape[self.right_start:self.right_end]
            left_ear = eye_aspect_ratio(left_eye)
            right_ear = eye_aspect_ratio(right_eye)
            ear = (left_ear + right_ear) / 2.0

            return ear, left_eye, right_eye
        return None, None, None
