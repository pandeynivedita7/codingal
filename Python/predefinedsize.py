import cv2

# Step 1: Load the original image
image_path = "road.jpg"  # Replace with your image file
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found.")
    exit()

# Step 2: Define target sizes (width x height)
sizes = {
    "small": (320, 240),
    "medium": (640, 480),
    "large": (1024, 768)
}

# Step 3: Resize, display, and save each version
for label, size in sizes.items():
    resized_image = cv2.resize(image, size)

    # Display the resized image
    window_name = f"{label.capitalize()} Image"
    cv2.imshow(window_name, resized_image)

    # Save the resized image
    output_filename = f"{label}_resized.jpg"
    cv2.imwrite(output_filename, resized_image)
    print(f"Saved: {output_filename}")

# Wait for a key press and close all image windows
cv2.waitKey(0)
cv2.destroyAllWindows()
