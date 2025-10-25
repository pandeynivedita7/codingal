import cv2
import numpy as np

# Define HSV range for hand/marker (adjust depending on your setup)
# Example: for green glove/marker
lower_color = np.array([35, 80, 40])
upper_color = np.array([85, 255, 255])

# Open webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

# Canvas for drawing
canvas = np.zeros((480, 640, 3), dtype=np.uint8)
drawing = False  # Drawing mode flag
shape_x, shape_y = 320, 240  # Shape initial position

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)  # Mirror for natural interaction
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create mask for color filtering
    mask = cv2.inRange(hsv, lower_color, upper_color)
    mask = cv2.GaussianBlur(mask, (7, 7), 0)

    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        # Take largest contour (likely the hand/marker)
        contour = max(contours, key=cv2.contourArea)
        
        if cv2.contourArea(contour) > 1000:
            # Draw contour
            cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)
            
            # Convex hull for finger detection
            hull = cv2.convexHull(contour)
            cv2.drawContours(frame, [hull], -1, (255, 0, 0), 2)
            
            # Get bounding box + centroid
            x, y, w, h = cv2.boundingRect(contour)
            cx, cy = x + w // 2, y + h // 2
            cv2.circle(frame, (cx, cy), 8, (0, 0, 255), -1)

            # Gesture logic based on bounding box height
            if h > 180:  
                drawing = True   # Large hand (open palm) → start drawing
            else:
                drawing = False  # Small contour (fist/marker) → stop drawing

            # Perform actions
            if drawing:
                cv2.circle(canvas, (cx, cy), 5, (0, 255, 0), -1)  # Draw line
            else:
                shape_x, shape_y = cx, cy  # Move shape with marker
    
    # Overlay canvas on frame
    output = cv2.add(frame, canvas)
    
    # Draw controlled shape
    cv2.circle(output, (shape_x, shape_y), 30, (255, 0, 255), -1)

    cv2.imshow("Gesture Control", output)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):  # Quit
        break
    elif key == ord("c"):  # Clear canvas
        canvas = np.zeros((480, 640, 3), dtype=np.uint8)

cap.release()
cv2.destroyAllWindows()
