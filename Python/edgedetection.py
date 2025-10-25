import cv2
import numpy as np #array

# Load an image in grayscale
image = cv2.imread('road.jpg', cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Image not found. Please check the filename.")
    exit()

# ---------------------- Filtering ----------------------

# Gaussian Filter
gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)

# Median Filter
median_blur = cv2.medianBlur(image, 5)

# ---------------------- Sobel Edge Detection ----------------------

# Sobel X and Y edge detection
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)#kernel size fold
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

# Magnitude of gradient
sobel_combined = cv2.magnitude(sobel_x, sobel_y)
sobel_combined = cv2.convertScaleAbs(sobel_combined)

# ---------------------- Canny Edge Detection ----------------------

# Apply Canny (lower threshold, upper threshold)
canny_edges = cv2.Canny(image, 100, 200)

# ---------------------- Display Results ----------------------

cv2.imshow('Original Image', image)
cv2.imshow('Gaussian Blur', gaussian_blur)
cv2.imshow('Median Blur', median_blur)
cv2.imshow('Sobel Edge Detection', sobel_combined)
cv2.imshow('Canny Edge Detection', canny_edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
