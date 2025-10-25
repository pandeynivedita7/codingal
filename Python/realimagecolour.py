import cv2
import numpy as np# handle array as images numerical opeartion

# ---------------------------
# 1.  Helper – filter logic
# ---------------------------
def apply_filter(image: np.ndarray, filter_type: str) -> np.ndarray:#def apply_filter(image, filter_type):
    """Return a copy of *image* with the selected filter applied."""
    if filter_type == "original":
        return image.copy()#Returns an unmodified copy of the original image.

    #
    # Start from a copy so the original never changes
    filtered = image.copy()

    if filter_type == "red_tint":
        filtered[:, :, 1] = 0          # zero-out green (120,60,200) original image colour(0,0,200)
        filtered[:, :, 0] = 0          # zero-out blue
    elif filter_type == "green_tint":
        filtered[:, :, 2] = 0          # zero-out red
        filtered[:, :, 0] = 0          # zero-out blue
    elif filter_type == "blue_tint":
        filtered[:, :, 2] = 0          # zero-out red
        filtered[:, :, 1] = 0          # zero-out green
    elif filter_type == "sobel":
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        combined = cv2.bitwise_or(sobelx.astype("uint8"), sobely.astype("uint8"))#bitwiseor
        filtered = cv2.cvtColor(combined, cv2.COLOR_GRAY2BGR)
    elif filter_type == "canny":
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)   # adjust thresholds as you like
        filtered = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    return filtered

#def apply_filter(image: np.ndarray, filter_type: str) -> np.ndarray: function def image(h,w,c numpy shape) filter_type( red,sobel)
# ->return type int
# ---------------------------
# 2.  Main – interactive loop
# ---------------------------
def main():
    image_path = "road.jpg"         # 🔁 change to the file you want
    image = cv2.imread(image_path)

    if image is None:
        print("[ERROR] Image not found – check the path.")
        return

    print("Controls:")
    print("    r – Red tint")
    print("    g – Green tint")
    print("    b – Blue tint")
    print("    s – Sobel edge detection")
    print("    c – Canny edge detection")
    print("    o – Original (remove filter)")
    print("    q – Quit")

    current_filter = "original"

    while True:
        filtered_frame = apply_filter(image, current_filter)
        cv2.imshow("Filtered image", filtered_frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
        elif key == ord("r"):
            current_filter = "red_tint"
        elif key == ord("g"):
            current_filter = "green_tint"
        elif key == ord("b"):
            current_filter = "blue_tint"
        elif key == ord("s"):
            current_filter = "sobel"
        elif key == ord("c"):
            current_filter = "canny"
        elif key == ord("o"):
            current_filter = "original"

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
