import cv2

# Load an image (replace 'test.jpg' with your own image path)
image = cv2.imread('road.jpg')

# Check if the image was loaded successfully
if image is None:
    print("Error: Image not found or failed to load.")
else:
    print("Image loaded successfully.")

    # Display the image in a window
    cv2.imshow('Test Image', image)

    # Wait for a key press indefinitely
    cv2.waitKey(0)

    # Close all OpenCV windows
    cv2.destroyAllWindows()
