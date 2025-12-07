# Color Conversions and Cropping

import cv2
import matplotlib.pyplot as plt

# Load image in BGR format (default in OpenCV)
image = cv2.imread('road.jpg')

# ✅ Check if image was loaded successfully
if image is None:
    print("Error: Image not found or path is incorrect.")
else:
    # ✅ Convert BGR to RGB for correct display in Matplotlib
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.title("RGB Image")
    plt.axis('off')  # Hide axis
    plt.show()

    # ✅ Convert BGR to Grayscale (not RGB to Grayscale)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    plt.imshow(gray_image, cmap='gray')
    plt.title("Grayscale Image")
    plt.axis('off')
    plt.show()

    # ✅ Crop image using NumPy slicing: rows 100–299, columns 200–399
    cropped_image = image[100:300, 200:400]# [] list slicing
    
    # Convert cropped image to RGB for correct color display
    cropped_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
    plt.imshow(cropped_rgb)
    plt.title("Cropped Region")
    plt.axis('off')
    plt.show()