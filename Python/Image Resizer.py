import cv2

# Load the image
image_path = "road.jpg"   # Change this to your image name
image = cv2.imread(image_path)

if image is None:
    print("Error: Could not load image.")
    exit()

# Predefined resize dimensions
sizes = {
    "small": (320, 240),
    "medium": (640, 480),
    "large": (1024, 768)
}

# Process each size
for label, (w, h) in sizes.items():
    resized = cv2.resize(image, (w, h))

    # Display the image
    cv2.imshow(f"{label} image", resized)
    cv2.waitKey(500)   # Shows each image for 0.5 sec

    # Save the resized image
    output_name = f"{label}_resized.jpg"
    cv2.imwrite(output_name, resized)
    print(f"Saved: {output_name}")

cv2.destroyAllWindows()
