from ultralytics import YOLO
import cv2

# Load YOLOv8 Nano (auto-downloads if not present)
model = YOLO("yolov8n.pt")

# Open webcam
cap = cv2.VideoCapture(0)

def run_edge_inference(frame):
    results = model(frame, conf=0.25)
    detections = []

    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf)
            cls = int(box.cls)

            detections.append({
                "bbox": (x1, y1, x2, y2),
                "confidence": conf,
                "class": cls
            })

            # Draw bounding box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            label = f"{model.names[cls]} {conf:.2f}"
            cv2.putText(frame, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        (0, 255, 0), 2)

    return frame, detections


while True:
    ret, frame = cap.read()
    if not ret:
        break

    output_frame, detections = run_edge_inference(frame)

    cv2.imshow("Edge YOLO Inference", output_frame)

    # Press ESC to exit
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
