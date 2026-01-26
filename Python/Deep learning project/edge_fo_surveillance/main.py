from ultralytics import YOLO
import cv2
import pickle
import numpy as np
import matplotlib.pyplot as plt
import time

# ---------------- BANDWIDTH METRICS ----------------
full_bw = []      # Baseline: full frame bandwidth (KB)
acato_bw = []     # Proposed: cropped ROI bandwidth (KB)

# ---------------- ENCRYPTION ----------------

from edge_fo_surveillance.fog.fog_refinement import fog_refine
from edge_fo_surveillance.fog.anomaly_detection import TemporalAnomalyDetector
from edge_fo_surveillance.utils.encryption import (
    generate_key,
    encrypt_data,
    decrypt_data
)



# ---------------- CONFIG ----------------
CONF_THRESHOLD = 0.6
model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture(0)

detector = TemporalAnomalyDetector()
SHARED_KEY = generate_key()

# ---------------- METRICS ----------------
edge_conf_history = []
fog_conf_history = []
enc_times = []

# ---------------- FUNCTIONS ----------------
def confidence_aware_offloading(detections):
    local, offload = [], []
    for d in detections:
        if d["confidence"] >= CONF_THRESHOLD:
            local.append(d)
        else:
            offload.append(d)
    return local, offload

def crop_regions(frame, offload):
    crops = []
    for d in offload:
        x1, y1, x2, y2 = d["bbox"]
        crop = frame[y1:y2, x1:x2]
        if crop.size > 0:
            crops.append(crop)
    return crops

# ---------------- MAIN LOOP ----------------
frame_id = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # ---------- BASELINE BANDWIDTH (FULL FRAME) ----------
    full_bw.append(frame.nbytes / 1024)  # KB per frame

    # ---------- EDGE YOLO INFERENCE ----------
    results = model(frame, conf=0.25)
    detections = []

    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            detections.append({
                "bbox": (x1, y1, x2, y2),
                "confidence": float(box.conf)
            })

    # ---------- ACATO ----------
    local, offload = confidence_aware_offloading(detections)

    if offload:
        edge_conf_history.append(
            np.mean([d["confidence"] for d in offload])
        )

    # ---------- EDGE → FOG ----------
    crops = crop_regions(frame, offload)
    refined = []

    if crops:
        encrypted_payloads = []
        total_crop_bytes = 0

        for crop in crops:
            crop_bytes = pickle.dumps(crop)

            start_enc = time.time()
            nonce, ciphertext = encrypt_data(crop_bytes, SHARED_KEY)
            enc_times.append(time.time() - start_enc)

            encrypted_payloads.append((nonce, ciphertext))
            total_crop_bytes += len(ciphertext)

        # Store ACATO bandwidth
        acato_bw.append(total_crop_bytes / 1024)

        # ---------- FOG REFINEMENT ----------
        refined = fog_refine(encrypted_payloads, SHARED_KEY)

        if refined:
            fog_conf_history.append(
                np.mean([d["confidence"] for d in refined])
            )

        print(f"[FOG] Frame {frame_id}: Refined detections = {len(refined)}")

    else:
        acato_bw.append(0)
        print(f"[FOG] Frame {frame_id}: No offloaded detections")

    # ---------- ANOMALY DETECTION ----------
    is_anomaly = detector.detect_anomaly(refined)

    if is_anomaly:
        print(f"⚠️ [ANOMALY] Detected at frame {frame_id}")
        cv2.putText(frame,
                    "ANOMALY DETECTED",
                    (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.0,
                    (0, 0, 255),
                    3)

    frame_id += 1

    cv2.imshow("Edge–Fog Surveillance System", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

# ---------------- CLEANUP ----------------
cap.release()
cv2.destroyAllWindows()

# ---------------- RESULTS ----------------
print("\nAccuracy Comparison Table")
print("-" * 40)

if edge_conf_history:
    print(f"Average Edge Confidence (Before Fog): {np.mean(edge_conf_history):.3f}")
else:
    print("Average Edge Confidence (Before Fog): N/A")

if fog_conf_history:
    print(f"Average Fog Confidence (After Fog):  {np.mean(fog_conf_history):.3f}")
else:
    print("Average Fog Confidence (After Fog):  N/A")

if enc_times:
    print(f"Average Encryption Time (ms): {np.mean(enc_times) * 1000:.3f}")

print("\nBandwidth Consumption Analysis")
print("-" * 40)

print(f"Average Full Frame Bandwidth (KB): {np.mean(full_bw):.2f}")
print(f"Average ACATO Bandwidth (KB):      {np.mean(acato_bw):.2f}")

reduction = (1 - np.mean(acato_bw) / np.mean(full_bw)) * 100
print(f"Bandwidth Reduction (%):           {reduction:.2f}%")

# ---------------- PLOTS ----------------
if edge_conf_history and fog_conf_history:
    plt.figure()
    plt.plot(edge_conf_history, label="Before Fog (Edge)")
    plt.plot(fog_conf_history, label="After Fog (Fog)")
    plt.xlabel("Frame Index")
    plt.ylabel("Average Detection Confidence")
    plt.title("Accuracy Improvement Before vs After Fog")
    plt.legend()
    plt.grid(True)
    plt.show()

plt.figure()
plt.plot(full_bw, label="Full Frame Upload (Baseline)")
plt.plot(acato_bw, label="ACATO (Cropped & Encrypted)")
plt.xlabel("Frame Index")
plt.ylabel("Bandwidth (KB)")
plt.title("Bandwidth Consumption: Baseline vs ACATO")
plt.legend()
plt.grid(True)
plt.show()
