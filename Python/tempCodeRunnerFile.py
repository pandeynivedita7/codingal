import cv2
import numpy as np
import pyautogui
import screen_brightness_control as sbc

cap = cv2.VideoCapture(0)

prev_y = None
prev_x = None

pyautogui.FAILSAFE = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    roi = frame[100:400, 300:600]  # Region of Interest
    cv2.rectangle(frame, (300,100), (600,400), (0,255,0), 2)

    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7,7), 0)

    _, thresh = cv2.threshold(blur, 80, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        cnt = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(cnt)

        if area > 3000:
            x,y,w,h = cv2.boundingRect(cnt)
            cx = x + w // 2
            cy = y + h // 2

            cv2.circle(roi, (cx, cy), 7, (0,0,255), -1)

            if prev_y is not None and prev_x is not None:
                dy = prev_y - cy
                dx = cx - prev_x

                # VOLUME / BRIGHTNESS (UP & DOWN)
                if abs(dy) > 20:
                    if area > 12000:
                        brightness = sbc.get_brightness()[0]
                        brightness = min(100, max(0, brightness + (5 if dy > 0 else -5)))
                        sbc.set_brightness(brightness)
                        cv2.putText(frame, "Brightness Control", (10,30),
                                   cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0), 2)
                    else:
                        if dy > 0:
                            pyautogui.press("volumeup")
                        else:
                            pyautogui.press("volumedown")
                        cv2.putText(frame, "Volume Control", (10,30),
                                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

                # SCROLL LEFT & RIGHT
                if abs(dx) > 25:
                    if dx > 0:
                        pyautogui.scroll(-100)
                        cv2.putText(frame, "Scroll Down", (10,70),
                                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
                    else:
                        pyautogui.scroll(100)
                        cv2.putText(frame, "Scroll Up", (10,70),
                                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

            prev_y = cy
            prev_x = cx

    cv2.imshow("Hand Gesture Control (No MediaPipe)", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
