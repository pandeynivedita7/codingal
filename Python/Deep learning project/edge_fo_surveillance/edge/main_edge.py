from ultralytics import YOLO
import cv2
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from edge_fo_surveillance.utils.encryption import encrypt_data

# ---------------- CONFIG ----------------
CONF_THRESHOLD = 0.6
MODEL_PATH = "yolov8n.pt"

# ---------------- ACATO LOGIC ----------------
def acato_decision(results, threshold):
    """
    Splits detections into local (edge) and offload (fog)
    based on confidence threshold
    """
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

# ---------------- MAIN ----------------
def main():
    print("[EDGE] Starting Edge Node")

    model = YOLO(MODEL_PATH)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ Camera not available")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # YOLO inference
        results = model(frame, conf=0.25, verbose=False)

        # ACATO decision
        local_boxes, offload_boxes = acato_decision(results, CONF_THRESHOLD)

        # ✅ REQUIRED CONSOLE OUTPUT
        print(f"[EDGE] Local: {len(local_boxes)} | Offload: {len(offload_boxes)}")

        # Draw EDGE detections (GREEN)
        for (x1, y1, x2, y2, conf) in local_boxes:
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(
                frame,
                f"EDGE {conf:.2f}",
                (x1, y1 - 8),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 0),
                2
            )

        # Draw FOG detections (RED)
        for (x1, y1, x2, y2, conf) in offload_boxes:
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.putText(
                frame,
                f"FOG {conf:.2f}",
                (x1, y1 - 8),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 0, 255),
                2
            )

        cv2.imshow("ACATO Edge Inference", frame)

        # ESC to exit
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

# ---------------- ENTRY ----------------
if __name__ == "__main__":
    main()
