import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7, 7), 0)

    _, thresh = cv2.threshold(blur, 80, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        cnt = max(contours, key=lambda x: cv2.contourArea(x))
        hull = cv2.convexHull(cnt)

        cv2.drawContours(frame, [cnt], -1, (0, 255, 0), 2)
        cv2.drawContours(frame, [hull], -1, (255, 0, 0), 2)

        hull = cv2.convexHull(cnt, returnPoints=False)
        if hull is not None and len(hull) > 3:
            defects = cv2.convexityDefects(cnt, hull)

            if defects is not None:
                count_defects = 0
                for i in range(defects.shape[0]):
                    s, e, f, d = defects[i, 0]
                    start = tuple(cnt[s][0])
                    end = tuple(cnt[e][0])
                    far = tuple(cnt[f][0])

                    a = np.linalg.norm(np.array(end) - np.array(start))
                    b = np.linalg.norm(np.array(far) - np.array(start))
                    c = np.linalg.norm(np.array(end) - np.array(far))
                    angle = (b**2 + c**2 - a**2) / (2*b*c)

                    if angle <= np.cos(90 * np.pi / 180):
                        count_defects += 1
                        cv2.circle(frame, far, 5, (0, 0, 255), -1)

                if count_defects >= 4:
                    cv2.putText(frame, "Hand Open", (50, 50),  cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
                else:
                    cv2.putText(frame, "Hand Closed", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    cv2.imshow("Hand Gesture", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
