import cv2
import numpy as np
import math
import os

def count_fingers(thresh, drawing):
    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) == 0:
        return 0

    cnt = max(contours, key=lambda x: cv2.contourArea(x))
    hull = cv2.convexHull(cnt)
    
    # Draw contours
    cv2.drawContours(drawing, [cnt], 0, (0, 255, 0), 2)
    cv2.drawContours(drawing, [hull], 0, (0, 0, 255), 2)
    
    # Convex hull and defects
    hull_indices = cv2.convexHull(cnt, returnPoints=False)
    defects = cv2.convexityDefects(cnt, hull_indices)
    
    if defects is None:
        return 0
    
    finger_count = 0

    for i in range(defects.shape[0]):
        s, e, f, d = defects[i, 0]
        start = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        far = tuple(cnt[f][0])

        # Using cosine rule to find angle
        a = math.dist(end, start)
        b = math.dist(far, start)
        c = math.dist(end, far)
        angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57

        if angle <= 90:
            finger_count += 1
            cv2.circle(drawing, far, 4, [0, 0, 255], -1)

    return finger_count + 1  # add one for the thumb

# Start video capture
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    roi = frame[100:400, 100:400]  # Define region of interest
    cv2.rectangle(frame, (100, 100), (400, 400), (0, 255, 0), 2)
    
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    # Define skin color range in HSV
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)

    # Mask skin color
    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    # Noise reduction
    mask = cv2.GaussianBlur(mask, (5, 5), 0)

    # Thresholding and finger counting
    drawing = np.zeros(roi.shape, np.uint8)
    fingers = count_fingers(mask, drawing)

    cv2.putText(frame, f"Fingers: {fingers}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
                1, (255, 0, 0), 2, cv2.LINE_AA)

    # Simple gesture controls
    if fingers == 1:
        print("Gesture: One finger - [Action: Open Notepad]")
        # os.system("notepad")  # Uncomment for real control

    elif fingers == 2:
        print("Gesture: Two fingers - [Action: Close app]")

    cv2.imshow("Gesture", frame)
    cv2.imshow("Threshold", mask)
    cv2.imshow("Hand", drawing)

    if cv2.waitKey(1) == 27:  # Press 'ESC' to exit
        break

cap.release()
cv2.destroyAllWindows()
