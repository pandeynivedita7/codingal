import cv2
import mediapipe as mp
import numpy as np
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from math import hypot
import screen_brightness_control as sbc

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7, max_num_hands=2)
mp_draw = mp.solutions.drawing_utils

# Pycaw for volume control
try:
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)
    volume_range = volume.GetVolumeRange()
    min_vol = volume_range[0]
    max_vol = volume_range[1]
except Exception as e:
    print(f"Error initializing Pycaw: {e}")
    exit()

# OpenCV Camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    
    if results.multi_hand_landmarks and results.multi_handedness:
        for hand_landmarks, hand_handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            label = hand_handedness.classification[0].label  # "Left" or "Right"
            
            # Draw landmarks
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Extract coordinates
            lm_list = []
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, c = frame.shape
                lm_list.append((int(lm.x * w), int(lm.y * h)))
            
            if lm_list:
                x1, y1 = lm_list[4]   # Thumb tip
                x2, y2 = lm_list[8]   # Index finger tip
                
                # Draw thumb-index connection
                cv2.circle(frame, (x1, y1), 10, (255, 0, 0), -1)
                cv2.circle(frame, (x2, y2), 10, (255, 0, 0), -1)
                cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
                
                # Distance between thumb & index
                length = hypot(x2 - x1, y2 - y1)
                
                if label == "Right":  # Control Volume
                    vol = np.interp(length, [20, 200], [min_vol, max_vol])
                    volume.SetMasterVolumeLevel(vol, None)
                    cv2.putText(frame, f'Volume: {int(np.interp(vol, [min_vol, max_vol], [0,100]))}%', 
                                (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3)
                
                elif label == "Left":  # Control Brightness
                    bright = np.interp(length, [20, 200], [0, 100])
                    sbc.set_brightness(int(bright))
                    cv2.putText(frame, f'Brightness: {int(bright)}%', 
                                (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 3)
    
    cv2.imshow("Gesture Volume & Brightness Control", frame)
    
    if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
