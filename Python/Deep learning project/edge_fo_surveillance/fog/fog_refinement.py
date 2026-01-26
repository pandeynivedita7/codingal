import pickle
import time
from ultralytics import YOLO
from edge_fo_surveillance.utils.encryption import decrypt_data

# Fog-level YOLO (heavier model)
fog_model = YOLO("yolov8m.pt")

def fog_refine(encrypted_payloads, key):
    """
    Decrypts ROIs received from edge and refines detections using fog-level YOLO
    """
    refined_detections = []
    dec_times = []

    for nonce, ciphertext in encrypted_payloads:
        # ---------- DECRYPT ----------
        start_dec = time.time()
        crop_bytes = decrypt_data(nonce, ciphertext, key)
        dec_times.append(time.time() - start_dec)

        crop = pickle.loads(crop_bytes)

        # ---------- FOG INFERENCE ----------
        results = fog_model(crop, conf=0.4)

        for r in results:
            for box in r.boxes:
                refined_detections.append({
                    "bbox": tuple(map(int, box.xyxy[0])),
                    "confidence": float(box.conf[0]),
                    "class": int(box.cls[0])
                })

    if dec_times:
        print(f"[FOG] Avg decryption time (ms): {(sum(dec_times)/len(dec_times))*1000:.3f}")

    return refined_detections
