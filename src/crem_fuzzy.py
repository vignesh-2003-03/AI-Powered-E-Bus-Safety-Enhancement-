# crem_fuzzy.py
import time
import cv2

EYE_AR_THRESH = 0.31
CLOSED_EYES_DURATION_THRESHOLD = 10
BLINK_DURATION_THRESHOLD = 2
RESET_INTERVAL = 3  # seconds

class CREMFuzzy:
    def __init__(self):
        self.closed_start_time = None
        self.prev_state = None
        self.last_reset_time = time.time()

    def process_ear(self, ear, frame, serial_comm=None):
        state = None
        if ear is None:
            return None

        if ear < EYE_AR_THRESH:
            if self.closed_start_time is None:
                self.closed_start_time = time.time()
            else:
                elapsed = time.time() - self.closed_start_time
                if elapsed >= CLOSED_EYES_DURATION_THRESHOLD:
                    cv2.putText(frame, "DROWSINESS ALERT!", (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    state = "drowsy"
                elif elapsed >= BLINK_DURATION_THRESHOLD:
                    cv2.putText(frame, "Eyes Closed", (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    state = "alert"
        elif ear > (EYE_AR_THRESH + 0.03):
            state = "run"
            self.closed_start_time = None
        else:
            self.closed_start_time = None

        # reset state
        if time.time() - self.last_reset_time >= RESET_INTERVAL:
            self.prev_state = None
            self.last_reset_time = time.time()

        # Only send new state if changed
        if state and state != self.prev_state:
            if serial_comm:
                serial_comm.send(state)
            self.prev_state = state

        cv2.putText(frame, "VAL: {:.3f}".format(ear), (300, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        return state