import cv2
import numpy as np
import os

# ---------------- PATHS ----------------
IMG_DIR = "data/edge1/images/train"
LBL_DIR = "data/edge1/labels/train"

os.makedirs(IMG_DIR, exist_ok=True)
os.makedirs(LBL_DIR, exist_ok=True)

# ---------------- IMAGE CONFIG ----------------
WIDTH, HEIGHT = 640, 480

# Create gray background (camera-like)
image = np.full((HEIGHT, WIDTH, 3), 180, dtype=np.uint8)

# YOLO label: 0 0.5 0.5 0.4 0.6
class_id = 0
x_center, y_center = 0.5, 0.5
box_w, box_h = 0.4, 0.6

# Convert YOLO → pixel coordinates
bw = int(box_w * WIDTH)
bh = int(box_h * HEIGHT)
xc = int(x_center * WIDTH)
yc = int(y_center * HEIGHT)

x1 = xc - bw // 2
y1 = yc - bh // 2
x2 = xc + bw // 2
y2 = yc + bh // 2

# ---------------- DRAW PERSON ----------------
# Filled rectangle = person body
cv2.rectangle(image, (x1, y1), (x2, y2), (255, 255, 255), -1)

# Optional: draw bounding box border (visual clarity)
cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

# Label text
cv2.putText(
    image,
    "person",
    (x1, y1 - 10),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.8,
    (0, 0, 255),
    2
)

# ---------------- SAVE FILES ----------------
img_path = os.path.join(IMG_DIR, "frame1.jpg")
lbl_path = os.path.join(LBL_DIR, "frame1.txt")

cv2.imwrite(img_path, image)

with open(lbl_path, "w") as f:
    f.write("0 0.5 0.5 0.4 0.6\n")

print("✅ Synthetic image with bounding box created")
print("📷 Image:", img_path)
print("📄 Label:", lbl_path)
