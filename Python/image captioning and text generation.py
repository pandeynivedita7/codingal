# ===============================
# 📦 Install Required Libraries
# ===============================
!pip install pillow requests colorama

# ===============================
# 🔐 Hugging Face API Key Setup
# ===============================
# Paste your Hugging Face API Key here 👇
HF_API_KEY = "your_huggingface_api_key"  # Replace this with your actual key

# ===============================
# 📚 Imports
# ===============================
import requests
from PIL import Image
import io
import os
from colorama import init, Fore, Style
import json

init(autoreset=True)  # Initialize Colorama

# ===============================
# 🔧 Helper: Send API Request
# ===============================
def query_hf_api(api_url, payload=None, files=None, method="post"):
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    try:
        if method.lower() == "post":
            response = requests.post(api_url, headers=headers, json=payload, files=files)
        else:
            response = requests.get(api_url, headers=headers, params=payload)
        if response.status_code != 200:
            raise Exception(f"Status {response.status_code}: {response.text}")
        return response.content
    except Exception as e:
        print(f"{Fore.RED}❌ Error while calling API: {e}")
        raise

# ===============================
# 🖼️ Get Basic Caption from Image
# ===============================
def get_basic_caption(image, model="nlpconnect/vit-gpt2-image-captioning"):
    print(f"{Fore.YELLOW}📸 Generating basic caption using vit-gpt2-image-captioning ...")
    api_url = f"https://api-inference.huggingface.co/models/{model}"
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    buffered.seek(0)
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    response = requests.post(api_url, headers=headers, data=buffered.read())
    result = response.json()
    if isinstance(result, dict) and "error" in result:
        return f"[Error] {result['error']}"
    return result[0].get("generated_text", "No caption generated.")

# ===============================
# ✍️ Generate Text from Prompt
# ===============================
def generate_text(prompt, model="gpt2", max_new_tokens=60):
    print(f"{Fore.CYAN}📝 Generating text with prompt: {prompt}")
    api_url = f"https://api-inference.huggingface.co/models/{model}"
    payload = {"inputs": prompt, "parameters": {"max_new_tokens": max_new_tokens}}
    text_bytes = query_hf_api(api_url, payload=payload)
    try:
        result = json.loads(text_bytes.decode("utf-8"))
    except Exception:
        raise Exception("Failed to decode text generation response.")
    if isinstance(result, dict) and "error" in result:
        raise Exception(result["error"])
    return result[0].get("generated_text", "")

# ===============================
# ✂️ Truncate text to N words
# ===============================
def truncate_text(text, word_limit):
    return " ".join(text.strip().split()[:word_limit])

# ===============================
# 🧪 Upload and Load Image
# ===============================
from google.colab import files
uploaded = files.upload()

image_path = list(uploaded.keys())[0]

if not os.path.exists(image_path):
    print(f"{Fore.RED}❌ File not found: {image_path}")
else:
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"{Fore.RED}❌ Failed to open image: {e}")

    # Basic caption
    basic_caption = get_basic_caption(image)
    print(f"{Fore.YELLOW}🖼️ Basic Caption: {Style.BRIGHT}{basic_caption}\n")

    # Menu
    def print_menu():
        print(f"""{Style.BRIGHT}
{Fore.GREEN}========== Image-to-Text ==========
1. Caption (5 words)
2. Description (30 words)
3. Summary (50 words)
4. Exit
""")

    while True:
        print_menu()
        choice = input(f"{Fore.CYAN}Enter your choice (1-4): {Style.RESET_ALL}")
        if choice == "1":
            caption = truncate_text(basic_caption, 5)
            print(f"{Fore.GREEN}✅ Caption (5 words): {Style.BRIGHT}{caption}\n")
        elif choice == "2":
            prompt_text = f"Expand the following caption into a detailed description in exactly 30 words: {basic_caption}"
            try:
                gen = generate_text(prompt_text, max_new_tokens=40)
                description = truncate_text(gen, 30)
                print(f"{Fore.GREEN}✅ Description (30 words): {Style.BRIGHT}{description}\n")
            except Exception as e:
                print(f"{Fore.RED}❌ Failed to generate description: {e}")
        elif choice == "3":
            prompt_text = f"Summarize the content of the image described by this caption into a summary of exactly 50 words: {basic_caption}"
            try:
                gen = generate_text(prompt_text, max_new_tokens=60)
                summary = truncate_text(gen, 50)
                print(f"{Fore.GREEN}✅ Summary (50 words): {Style.BRIGHT}{summary}\n")
            except Exception as e:
                print(f"{Fore.RED}❌ Failed to generate summary: {e}")
        elif choice == "4":
            print(f"{Fore.GREEN}👋 Goodbye!")
            break
        else:
            print(f"{Fore.RED}❌ Invalid choice. Enter 1-4 only.")
