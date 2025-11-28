import cv2
import mediapipe as mp
import numpy as np
import screen_brightness_control as sbc
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Initialize MediaPipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

# Audio Control Setup (Pycaw)
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]

# Start Webcam
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

            # Extract landmarks
            lmList = []
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                lmList.append((int(lm.x * w), int(lm.y * h)))

            x1, y1 = lmList[4]   # Thumb Tip
            x2, y2 = lmList[8]   # Index Finger Tip

            # Draw circles
            cv2.circle(img, (x1, y1), 10, (255,0,0), cv2.FILLED)
            cv2.circle(img, (x2, y2), 10, (255,0,0), cv2.FILLED)

            # Draw line
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # Distance
            length = np.hypot(x2 - x1, y2 - y1)

            # Volume Control Mapping
            vol = np.interp(length, [20, 150], [minVol, maxVol])
            volume.SetMasterVolumeLevel(vol, None)

            # Brightness Control Mapping
            bright = np.interp(length, [20, 150], [10, 100])
            sbc.set_brightness(int(bright))

            # Bar Display
            bar = int(np.interp(length, [20, 150], [400, 150]))
            cv2.rectangle(img, (50,150), (85,400), (0,255,0), 2)
            cv2.rectangle(img, (50,bar), (85,400), (0,255,0), cv2.FILLED)

            # Show percentage
            percent = int(np.interp(length, [20,150], [0,100]))
            cv2.putText(img, f'{percent}%', (40, 430), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (255,255,255), 3)

    cv2.imshow("Gesture Control", img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
