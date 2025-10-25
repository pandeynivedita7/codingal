import cv2#  image processing, video capture, and computer vision tasks.

# Load the pre-trained Haar Cascade Classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')# yolo

# Start capturing video from webcam (0 is the default webcam)
cap = cv2.VideoCapture(0)# 1 external camera

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    # Read each frame from the video feed
    ret, frame = cap.read()# ret indicates if the frame is captured successfully.frame holds the actual image from the video.
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces (returns a list of rectangles around detected faces)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40))

    # Draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display face count
    cv2.putText(frame, f'People Count: {len(faces)}', (10, 30),# frame image len(string no of faces)(10,30 coordinates)
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)#text, scale factor 1,red thickness 2

    # Show the frame with rectangles and count
    cv2.imshow('Real-Time Face Tracking & Counting', frame)

    # Break loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
