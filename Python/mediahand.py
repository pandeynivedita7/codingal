"""
Hand-gesture control for system volume (right hand) and screen brightness
(left hand) using MediaPipe, Pycaw and screen_brightness_control.

• Close the script with the **q** key.
• Works on Windows (Pycaw is Windows-only).
• Install requirements:
    pip install opencv-python mediapipe pycaw comtypes screen_brightness_control numpy
"""

import cv2
import mediapipe as mp
import numpy as np
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from math import hypot
import screen_brightness_control as sbc

# ────────────────────────────────────────────────────────────────
#  MediaPipe Hands
# ────────────────────────────────────────────────────────────────
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7,
)
mp_draw = mp.solutions.drawing_utils

# ────────────────────────────────────────────────────────────────
#  Pycaw for master-volume control
# ────────────────────────────────────────────────────────────────
try:
    devices   = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume    = interface.QueryInterface(IAudioEndpointVolume)
    min_vol, max_vol, _ = volume.GetVolumeRange()   # typically (-96.0, 0.0, 0.03)
except Exception as e:
    print(f"[!] Error initialising Pycaw — volume control disabled:\n    {e}")
    volume = None  # keep going so brightness still works
    min_vol = max_vol = 0.0

# ────────────────────────────────────────────────────────────────
#  Open webcam
# ────────────────────────────────────────────────────────────────
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise RuntimeError("Error: could not access the webcam.")

# ────────────────────────────────────────────────────────────────
#  Main loop
# ────────────────────────────────────────────────────────────────
try:
    while True:
        success, img = cap.read()
        if not success:
            print("Failed to read frame from webcam.")
            break

        img = cv2.flip(img, 1)                                # mirror
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)

        if results.multi_hand_landmarks and results.multi_handedness:
            for i, hand_landmarks in enumerate(results.multi_hand_landmarks):
                hand_label = results.multi_handedness[i].classification[0].label  # "Left" / "Right"
                mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Tip coordinates (normalised 0-1)
                thumb_tip  = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                index_tip  = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

                # Convert to pixel coords
                h, w, _ = img.shape
                thumb_pos = (int(thumb_tip.x * w),  int(thumb_tip.y * h))
                index_pos = (int(index_tip.x * w),  int(index_tip.y * h))

                # Visual helpers
                cv2.circle(img, thumb_pos, 10, (255, 0, 0), cv2.FILLED)
                cv2.circle(img, index_pos, 10, (255, 0, 0), cv2.FILLED)
                cv2.line(img, thumb_pos, index_pos, (0, 255, 0), 3)

                # Euclidean distance between tips (in pixels)
                distance = hypot(index_pos[0] - thumb_pos[0],
                                 index_pos[1] - thumb_pos[1])

                # ─────────── Right hand → system volume ────────────
                if hand_label == "Right" and volume is not None:
                    vol_level = np.interp(distance, [30, 300], [min_vol, max_vol])
                    try:
                        volume.SetMasterVolumeLevel(vol_level, None)
                    except Exception as e:
                        print(f"[!] Error adjusting volume: {e}")

                    # Volume bar (left side, blue)
                    vol_bar = int(np.interp(distance, [30, 300], [400, 150]))
                    cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 2)
                    cv2.rectangle(img, (50, vol_bar), (85, 400), (255, 0, 0), cv2.FILLED)
                    cv2.putText(
                        img,
                        f'Vol: {int(np.interp(distance, [30, 300], [0, 100]))}%',
                        (40, 450),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (255, 0, 0),
                        3,
                    )

                # ─────────── Left hand → screen brightness ─────────
                elif hand_label == "Left":
                    brightness = int(np.interp(distance, [30, 300], [0, 100]))
                    try:
                        sbc.set_brightness(brightness)
                    except Exception as e:
                        print(f"[!] Error adjusting brightness: {e}")

                    # Brightness bar (right side, green)
                    bright_bar = int(np.interp(distance, [30, 300], [400, 150]))
                    cv2.rectangle(img, (565, 150), (600, 400), (0, 255, 0), 2)
                    cv2.rectangle(img, (565, bright_bar), (600, 400), (0, 255, 0), cv2.FILLED)
                    cv2.putText(
                        img,
                        f'Brightness: {brightness}%',
                        (360, 450),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 255, 0),
                        3,
                    )

        cv2.imshow("Gesture-Based Volume & Brightness Control", img)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

finally:
    cap.release()
    cv2.destroyAllWindows()
