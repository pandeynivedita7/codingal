import requests
from PIL import Image
from io import BytesIO
from config import HF_API_KEY  # Your Hugging Face API key stored in config.py


def generate_inpainting_image(prompt, image_path, mask_path):
    """
    Generates a new image by inpainting masked regions of a given image.

    Parameters:
    - prompt (str): Description of the desired modification.
    - image_path (str): Path to the base image.
    - mask_path (str): Path to the mask image (white areas = regions to inpaint).

    Returns:
    - PIL.Image: The resulting inpainted image.
    """
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-inpainting"
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}

    # Read image and mask file content
    with open(image_path, "rb") as img_file:# open read() write append
        image_data = img_file.read()
    with open(mask_path, "rb") as mask_file:
        mask_data = mask_file.read()

    # Prepare the API request payload
    payload = {"inputs": prompt}# input
    files = {
        "image": ("image.png", image_data, "image/png"),
        "mask": ("mask.png", mask_data, "image/png")
    }

    # Send the request to Hugging Face API
    response = requests.post(API_URL, headers=headers, data=payload, files=files)

    if response.status_code == 200:
        # Load the resulting image from the response
        inpainted_image = Image.open(BytesIO(response.content))
        return inpainted_image
    else:
        raise Exception(f"Request failed with status code {response.status_code}: {response.text}")


def main():
    print("Welcome to the Inpainting and Restoration Challenge!")
    print("This activity allows you to restore or transform parts of an existing image.")
    print("Provide a base image, a mask indicating the areas to modify, and a text prompt describing the desired change.")
    print("Type 'exit' at any prompt to quit.\n")

    while True:
        prompt = input("Enter a description for the inpainting (or 'exit' to quit):\n")
        if prompt.lower() == 'exit':
            print("Goodbye!")
            break

        image_path = input("Enter the path to the base image (e.g., base_image.png):\n")
        if image_path.lower() == 'exit':
            break

        mask_path = input("Enter the path to the mask image (e.g., mask_image.png):\n")
        if mask_path.lower() == 'exit':
            break

        try:
            print("\nProcessing inpainting...")
            result_image = generate_inpainting_image(prompt, image_path, mask_path)
            result_image.show()  # Display the inpainted image

            save_option = input("Do you want to save the inpainted image? (yes/no): ").strip().lower()
            if save_option == 'yes':
                file_name = input("Enter a name for the image file (without extension): ").strip()
                result_image.save(f"{file_name}.png")
                print(f"Image saved as {file_name}.png\n")

            print("-" * 80 + "\n")
        except Exception as e:
            print("An error occurred:", e)


# Run the program
if __name__ == "__main__":
    main()
#Taking a base image
#Using a mask image (white = area to change)
#Applying a text prompt (what change to make)
#Sending this to Hugging Face’s Stable Diffusion Inpainting model
#Returning a new image with the change