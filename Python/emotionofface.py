import cv2
import time
from fer import FER# emotion detection

def draw_label(img, text, x, y):
    """Draws a nice label above the bounding box."""
    font = cv2.FONT_HERSHEY_SIMPLEX
    scale = 0.6
    thickness = 2
    (tw, th), _ = cv2.getTextSize(text, font, scale, thickness)
    cv2.rectangle(img, (x, y - th - 10), (x + tw + 10, y), (0, 0, 0), -1)
    cv2.putText(img, text, (x + 5, y - 5), font, scale, (255, 255, 255), thickness, cv2.LINE_AA)

def main():
    # Initialize webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Could not open webcam. Try a different index (1, 2) or check permissions.")
        return

    # FER detector (uses fast face detection internally; no GPU required)
    detector = FER(mtcnn=False)  # set True if you installed 'mtcnn' for potentially better face detection

    # For FPS display
    prev_time = time.time()
    fps = 0.0

    # Process every nth frame to keep it snappy on low-power machines
    stride = 1
    frame_idx = 0

    print("✅ Press ESC to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Failed to read frame from webcam.")
            break

        frame_idx += 1
        display_frame = frame.copy()

        # Optionally downscale for speed (keep display size same)
        # small = cv2.resize(frame, None, fx=0.75, fy=0.75)  # uncomment to speed up

        if frame_idx % stride == 0:
            # Detect faces & emotions on the full frame
            # FER returns a list of dicts: {'box': (x, y, w, h), 'emotions': {...}}
            results = detector.detect_emotions(frame)
        else:
            results = []

        # Draw results
        for r in results:
            (x, y, w, h) = r["box"]
            emotions = r["emotions"]
            if not emotions:
                continue
            # Highest-probability emotion
            top_emotion, score = max(emotions.items(), key=lambda kv: kv[1])
            # Bounding box
            cv2.rectangle(display_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # Label with emotion + confidence
            label = f"{top_emotion.upper()}  {int(score * 100)}%"
            draw_label(display_frame, label, x, y)

        # FPS calculation
        now = time.time()
        dt = now - prev_time
        if dt > 0:
            fps = 0.9 * fps + 0.1 * (1.0 / dt) if fps > 0 else (1.0 / dt)
        prev_time = now
        cv2.putText(display_frame, f"FPS: {fps:.1f}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

        cv2.imshow("Real-Time Emotion Detection (ESC to quit)", display_frame)

        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # ESC
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
