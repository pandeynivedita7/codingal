import cv2
from PIL import Image, ImageDraw, ImageFont

# Load an image using OpenCV
image = cv2.imread('road.jpg')  # Replace with your image path

# Resize image
resized = cv2.resize(image, (300, 300))

# Rotate image 90 degrees clockwise
rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

# Flip image horizontally
flipped = cv2.flip(image, 1)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Save grayscale as color image for text overlay using PIL
cv2.imwrite('temp_gray.jpg', gray)
pil_image = Image.open('temp_gray.jpg').convert("RGB")

# Draw text on the image
draw = ImageDraw.Draw(pil_image)
font = ImageFont.load_default()
draw.text((10, 10), "Nivedita", fill=(255, 0, 0), font=font)

# Save the final image
pil_image.save('output_image.jpg')

# Display images using OpenCV (optional)
cv2.imshow('Original', image)
cv2.imshow('Resized', resized)
cv2.imshow('Rotated', rotated)
cv2.imshow('Flipped', flipped)
cv2.imshow('Grayscale + Text', cv2.imread('output_image.jpg'))

cv2.waitKey(0)
cv2.destroyAllWindows()
