# main.py
import cv2
import imutils
from detection import EyeDetector
from crem_fuzzy import CREMFuzzy
from serial_comm import SerialComm

def main():
    detector = EyeDetector()
    crem = CREMFuzzy()
    serial_comm = SerialComm(port='COM6', baudrate=115200)

    print("[INFO] Starting video stream...")
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = imutils.resize(frame, width=600)
        frame = cv2.flip(frame, 1)

        ear, left_eye, right_eye = detector.detect_eyes(frame)
        state = crem.process_ear(ear, frame, serial_comm)

        cv2.putText(frame, "Press 'Esc' to exit", (10, 550),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
    serial_comm.close()

if __name__ == "__main__":
    main()
# main.py
import cv2
import imutils
from detection import EyeDetector
from crem_fuzzy import CREMFuzzy
from serial_comm import SerialComm

def main():
    detector = EyeDetector()
    crem = CREMFuzzy()
    serial_comm = SerialComm(port='COM6', baudrate=115200)

    print("[INFO] Starting video stream...")
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = imutils.resize(frame, width=600)
        frame = cv2.flip(frame, 1)

        ear, left_eye, right_eye = detector.detect_eyes(frame)
        state = crem.process_ear(ear, frame, serial_comm)

        cv2.putText(frame, "Press 'Esc' to exit", (10, 550),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
    serial_comm.close()

if __name__ == "__main__":
    main()
