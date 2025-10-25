import cv2# image preprocessing on imAage display,transform,change colour

# Load the image
image = cv2.imread('road.jpg')#() argument name of file 

# Convert the image to grayscale cvt convert 1color to another 0 black 255 white
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Resize the grayscale image to 224x224
resized_image = cv2.resize(gray_image, (224, 224))# dimesion target value size should be 224*224 (Argument)

# Display the resized grayscale image in a single window
cv2.imshow('Processed Image', resized_image)

# Wait for a key press
key = cv2.waitKey(0)  # Wait indefinitely for a key press

# Check if the "S" key was pressed (ASCII for 'S' is 83)
if key == ord('s'):
    # Save the processed image when "S" is pressed
    cv2.imwrite('grayscale_resized_image.jpg', resized_image)
    print("Image saved as grayscale_resized_image.jpg")
else:
    print("Image not saved")

# Close the window
cv2.destroyAllWindows()

# Print processed image properties
print(f"Processed Image Dimensions: {resized_image.shape}")
