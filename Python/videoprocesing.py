import cv2

# Load video (1-second video; assume 30 fps)
cap = cv2.VideoCapture("one_second_video.mp4")

# Get frame rate (frames per second)
fps = int(cap.get(cv2.CAP_PROP_FPS))
print("FPS:", fps)

# Read and process each frame
frame_number = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Apply Canny edge filter
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)

    # Display original and processed frame side by side
    combined = cv2.hconcat([gray, edges])
    cv2.imshow("Original vs Canny Edge", combined)

    key = cv2.waitKey(int(1000 / fps))  # Wait appropriate time between frames 1000/30 33.33ms
    if key == ord('q'):
        break

    frame_number += 1

print(f"Total frames processed: {frame_number}")
cap.release()
cv2.destroyAllWindows()
