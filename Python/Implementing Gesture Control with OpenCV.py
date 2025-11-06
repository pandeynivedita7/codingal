import cv2
import numpy as np

# Initialize webcam
cap = cv2.VideoCapture(0)

# Define color range for detection (e.g., green color)
# You can adjust these HSV values based on lighting and glove color
lower_color = np.array([40, 70, 70])      # Lower bound for green
upper_color = np.array([80, 255, 255])    # Upper bound for green

# Initial position of the moving circle
x, y = 300, 300
radius = 30

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip frame for natural interaction
    frame = cv2.flip(frame, 1)

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create mask for selected color
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Reduce noise
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        # Find the largest contour (hand)
        largest_contour = max(contours, key=cv2.contourArea)

        # Get bounding circle
        ((cx, cy), r) = cv2.minEnclosingCircle(largest_contour)

        # Only consider if radius is large enough
        if r > 20:
            x, y = int(cx), int(cy)
            cv2.circle(frame, (x, y), int(r), (0, 255, 0), 2)
            cv2.putText(frame, "Gesture Detected", (10, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Draw a movable circle controlled by gesture
    cv2.circle(frame, (x, y), radius, (255, 0, 0), -1)
    cv2.putText(frame, "Move the blue circle with your hand", (10, 460),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    # Show frames
    cv2.imshow("Gesture Control", frame)
    cv2.imshow("Mask", mask)

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
