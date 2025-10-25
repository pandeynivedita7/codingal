import cv2
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import img_to_array

# Load Haar Cascade for face detection
cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start video capture (webcam)
cap = cv2.VideoCapture(0)

# Load the pre-trained emotion recognition model
model = load_model('emotion_model.h5')

# List of emotions corresponding to model's output indices
emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# Show model architecture summary
model.summary()

# Check if the camera is accessible
if not cap.isOpened():
    print("Could not access camera.")
    exit()

# Infinite loop for live detection
while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        print("Frame could not be read.")
        break

    # Convert the frame to grayscale (as the model is trained on grayscale images)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))

    # Loop through all detected faces
    for (x, y, w, h) in faces:
        # Draw a rectangle around the detected face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Extract the face ROI (Region of Interest)
        roi = gray[y:y + h, x:x + w]

        # Resize ROI to 48x48 (input size expected by the model)
        roi_resized = cv2.resize(roi, (48, 48))

        # Normalize pixel values to [0, 1]
        roi_resized = roi_resized.astype("float32") / 255.0

        # Convert ROI to an array with shape (48, 48, 1)
        roi_resized = img_to_array(roi_resized)
        roi_resized = np.expand_dims(roi_resized, axis=0)

        # Predict emotion
        emotion_pred = model.predict(roi_resized)

        # Get index of the highest probability
        max_index = np.argmax(emotion_pred[0])
        predict = emotions[max_index]

        # Print raw probabilities for all emotions
        print("Prediction scores:", emotion_pred[0])

        # Display predicted emotion on the frame
        cv2.putText(frame, predict, (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)

    # Show the frame with rectangles and emotion text
    cv2.imshow("Face and Emotion Detection", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Exiting application...")
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
