import cv2
import mediapipe as mp
import time
import numpy as np

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Filters list
filters = [
    None,        # 0 - No filter
    "gray",      # 1 - Grayscale
    "sepia",     # 2 - Sepia
    "negative",  # 3 - Negative
    "blur"       # 4 - Blur
]

current_filter = 0
last_switch = time.time()

# Function to apply filters
def apply_filter(frame, filter_type):
    if filter_type == "gray":
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif filter_type == "sepia":
        kernel = np.array([[0.272, 0.534, 0.131],
                           [0.349, 0.686, 0.168],
                           [0.393, 0.769, 0.189]])
        return cv2.transform(frame, kernel)
    elif filter_type == "negative":
        return cv2.bitwise_not(frame)#logical or 
    elif filter_type == "blur":
        return cv2.GaussianBlur(frame, (25, 25), 0)
    else:
        return frame

# Capture webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip for natural interaction
    frame = cv2.flip(frame, 1)# mirror for natural interaction
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get coordinates of index finger tip
            index_finger_tip = hand_landmarks.landmark[8]
            h, w, c = frame.shape
            cx, cy = int(index_finger_tip.x * w), int(index_finger_tip.y * h)

            # Switch filter if index finger is near top
            if cy < 100 and time.time() - last_switch > 1:
                current_filter = (current_filter + 1) % len(filters)
                last_switch = time.time()

    # Apply filter
    filtered_frame = apply_filter(frame, filters[current_filter])

    # If grayscale, convert back to 3 channels for display
    if filters[current_filter] == "gray":
        filtered_frame = cv2.cvtColor(filtered_frame, cv2.COLOR_GRAY2BGR)

    # Display current filter name
    cv2.putText(filtered_frame, f"Filter: {filters[current_filter]}", (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show output
    cv2.imshow("Gesture Controlled Photo App", filtered_frame)

    # Save screenshot on pressing 's'
    key = cv2.waitKey(1)
    if key == ord('s'):
        filename = f"screenshot_{int(time.time())}.png"
        cv2.imwrite(filename, filtered_frame)
        print(f"Saved {filename}")
    elif key == 27:  # ESC key
        break

cap.release()
cv2.destroyAllWindows()
