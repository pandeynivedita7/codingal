import cv2# computer vision 2

# Load the image
image = cv2.imread('road.jpg')# load the image image processing

# Resize the window to a specific size without resizing the image
cv2.namedWindow('Loaded Image', cv2.WINDOW_NORMAL)  # Create a resizable window
cv2.resizeWindow('Loaded Image', 500, 500)  # Set the window size to 500x500 (width x height) pixel 500*500 pixels

# Display the image in the resized window
cv2.imshow('Loaded Image', image)# create a window to display the image
cv2.waitKey(0)  # Wait for a key press pause execution 0 means indefine untill wheni have to pause
cv2.destroyAllWindows()  # Close the window free the resource

# Print image properties
print(f"Image Dimensions: {image.shape}")  # Height, Width, Channels 3 properites 2 well know width andheight channel rgb


