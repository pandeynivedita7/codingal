from ultralytics import YOLO
import cv2

# Load the YOLO model (using a pretrained model, e.g., yolov8n.pt)
model = YOLO("yolov8n.pt")  # Replace with your custom model if needed

def detect_action_live(model):
    # Open the webcam (0 = default camera, change if using an external webcam)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Press 'q' to quit.")

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Perform object detection
        results = model.predict(source=frame, conf=0.25, save=False, show=False)

        # Visualize the results
        annotated_frame = results[0].plot()

        # Display the annotated frame
        cv2.imshow("Live Detection", annotated_frame)

        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close the window
    cap.release()
    cv2.destroyAllWindows()

# Run the live detection
detect_action_live(model)
