from ultralytics import YOLO
import cv2

# -----------------------------
# Configuration
# -----------------------------
CONF_THRESHOLD = 0.6
MODEL_PATH = "yolov8n.pt"

# -----------------------------
# Load YOLOv8 model
# -----------------------------
model = YOLO(MODEL_PATH)

# -----------------------------
# ACATO Decision Function
# Algorithm 2: Confidence-Aware Task Offloading
# -----------------------------
def acato_decision(results, threshold):
    local = []
    offload = []

    for r in results:
        for box in r.boxes:
            conf = float(box.conf[0])
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            if conf >= threshold:
                local.append((x1, y1, x2, y2, conf))
            else:
                offload.append((x1, y1, x2, y2, conf))

    return local, offload


# -----------------------------
# Video Capture (Webcam)
# -----------------------------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Camera not accessible")
    exit()

print("✅ Edge ACATO Live Inference Started (ESC to exit)")

# -----------------------------
# Main Edge Loop
# -----------------------------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # YOLO Inference
    results = model(frame, conf=0.25, verbose=False)

    # ACATO Decision
    local_boxes, offload_boxes = acato_decision(results, CONF_THRESHOLD)

    # -----------------------------
    # Draw Edge (Local) Detections
    # -----------------------------
    for (x1, y1, x2, y2, conf) in local_boxes:
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(
            frame,
            f"EDGE {conf:.2f}",
            (x1, y1 - 5),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 255, 0),
            2,
        )

    # -----------------------------
    # Draw Fog (Offloaded) Detections
    # -----------------------------
    for (x1, y1, x2, y2, conf) in offload_boxes:
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cv2.putText(
            frame,
            f"FOG {conf:.2f}",
            (x1, y1 - 5),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 0, 255),
            2,
        )

    # Display Frame
    cv2.imshow("ACATO Edge Live Inference", frame)

    # Exit on ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

# -----------------------------
# Cleanup
# -----------------------------
cap.release()
cv2.destroyAllWindows()
print("🛑 Edge inference stopped")
