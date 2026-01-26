# Gesture-Controlled Photo App with Real-Time Filters
# Requirements:
# pip install opencv-python mediapipe numpy

import cv2
import mediapipe as mp
import numpy as np
import time

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

# Webcam
cap = cv2.VideoCapture(0)

# Filter list
filters = ["NORMAL", "GRAYSCALE", "SEPIA", "NEGATIVE", "BLUR"]
filter_index = 0

# Capture control
last_action_time = 0
cooldown = 1.2  # seconds

# Helper functions
def apply_filter(img, filter_name):
    if filter_name == "GRAYSCALE":
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    elif filter_name == "SEPIA":
        kernel = np.array([[0.272, 0.534, 0.131],
                           [0.349, 0.686, 0.168],
                           [0.393, 0.769, 0.189]])
        sepia = cv2.transform(img, kernel)
        return np.clip(sepia, 0, 255).astype(np.uint8)
    elif filter_name == "NEGATIVE":
        return cv2.bitwise_not(img)
    elif filter_name == "BLUR":
        return cv2.GaussianBlur(img, (15, 15), 0)
    return img

def distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

photo_count = 0

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    h, w, _ = frame.shape

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lm = handLms.landmark

            # Landmark positions
            thumb = (int(lm[4].x * w), int(lm[4].y * h))
            index = (int(lm[8].x * w), int(lm[8].y * h))
            middle = (int(lm[12].x * w), int(lm[12].y * h))
            ring = (int(lm[16].x * w), int(lm[16].y * h))
            pinky = (int(lm[20].x * w), int(lm[20].y * h))

            d_index = distance(thumb, index)
            d_middle = distance(thumb, middle)
            d_ring = distance(thumb, ring)
            d_pinky = distance(thumb, pinky)

            current_time = time.time()

            # Gesture 1: Thumb + Index → Capture photo
            if d_index < 30 and (current_time - last_action_time) > cooldown:
                filename = f"photo_{photo_count}.png"
                cv2.imwrite(filename, frame)
                photo_count += 1
                last_action_time = current_time

            # Gesture 2: Thumb + Middle → Next filter
            elif d_middle < 30 and (current_time - last_action_time) > cooldown:
                filter_index = (filter_index + 1) % len(filters)
                last_action_time = current_time

            # Gesture 3: Thumb + Ring → Previous filter
            elif d_ring < 30 and (current_time - last_action_time) > cooldown:
                filter_index = (filter_index - 1) % len(filters)
                last_action_time = current_time

            # Gesture 4: Thumb + Pinky → Reset filter
            elif d_pinky < 30 and (current_time - last_action_time) > cooldown:
                filter_index = 0
                last_action_time = current_time

            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

    # Apply selected filter
    filtered = apply_filter(frame, filters[filter_index])

    # Display filter name
    cv2.putText(
        filtered if filters[filter_index] != "GRAYSCALE" else frame,
        f"Filter: {filters[filter_index]}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # Show output
    if filters[filter_index] == "GRAYSCALE":
        cv2.imshow("Gesture Photo App", filtered)
    else:
        cv2.imshow("Gesture Photo App", filtered)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
