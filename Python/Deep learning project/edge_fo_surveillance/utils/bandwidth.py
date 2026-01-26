from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt

CONF_THRESHOLD = 0.6
model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture(0)

full_bw = []
acato_bw = []

def confidence_aware_offloading(detections):
    local, offload = [], []
    for d in detections:
        if d["confidence"] >= CONF_THRESHOLD:
            local.append(d)
        else:
            offload.append(d)
    return local, offload

def calculate_bandwidth(frame, offload):
    h, w, _ = frame.shape
    full_frame_bytes = h * w * 3

    crop_bytes = 0
    for d in offload:
        x1, y1, x2, y2 = d["bbox"]
        crop_bytes += (x2 - x1) * (y2 - y1) * 3

    return full_frame_bytes, crop_bytes

frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, conf=0.25)
    detections = []

    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            detections.append({
                "bbox": (x1, y1, x2, y2),
                "confidence": float(box.conf)
            })

    local, offload = confidence_aware_offloading(detections)

    # 🔹 BANDWIDTH COMPUTATION (THIS WAS MISSING)
    full_frame_bytes, crop_bytes = calculate_bandwidth(frame, offload)

    full_bw.append(full_frame_bytes / 1024)   # KB
    acato_bw.append(crop_bytes / 1024)        # KB

    frame_count += 1

    if cv2.waitKey(1) & 0xFF == 27 or frame_count > 100:
        break

cap.release()
plt.plot(full_bw, label="Full-frame Upload (Baseline)")
plt.plot(acato_bw, label="ACATO Crop-based Upload")
plt.xlabel("Frame Number")
plt.ylabel("Bandwidth (KB)")
plt.title("Bandwidth Savings using Confidence-Aware Offloading")
plt.legend()
plt.grid(True)
plt.show()
