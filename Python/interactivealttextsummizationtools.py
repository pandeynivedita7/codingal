
# Description: Summarizes text using Hugging Face Inference API

import requests
import os
from colorama import Fore, Style, init

# Initialize colorama for colored output
init(autoreset=True)

# ---------------------------
# 1. Default Configuration
# ---------------------------
DEFAULT_MODEL = "google/pegasus-xsum"
API_KEY = os.getenv("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")  # Set your Hugging Face API key as environment variable

if not API_KEY:
    print(Fore.RED + "❌ Error: Hugging Face API key not found. Please set HF_API_KEY.")
    exit(1)


# ---------------------------
# 2. Build API URL Function
# ---------------------------
def build_api_url(model_name: str) -> str:
    return f"https://api-inference.huggingface.co/models/{model_name}"


# ---------------------------
# 3. API Query Function
# ---------------------------
def query_api(payload: dict, model_name: str = DEFAULT_MODEL) -> dict:
    url = build_api_url(model_name)
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        print(Fore.RED + f"❌ API Error: {response.status_code} - {response.text}")
        return None

    return response.json()


# ---------------------------
# 4. Summarization Function
# ---------------------------
def summarize_text(text: str, min_len: int, max_len: int, model_name: str = DEFAULT_MODEL):
    payload = {
        "inputs": text,
        "parameters": {
            "min_length": min_len,
            "max_length": max_len,
        },
    }

    print(Fore.CYAN + f"\n🔄 Summarizing with model: {model_name} ...")
    response = query_api(payload, model_name)

    if not response:
        print(Fore.RED + "❌ Failed to get a response from API.")
        return None

    # Expected response: [{'summary_text': '...'}]
    if isinstance(response, list) and "summary_text" in response[0]:
        return response[0]["summary_text"]
    else:
        print(Fore.RED + "❌ Unexpected API response format.")
        return None


# ---------------------------
# 5. Main Execution Flow
# ---------------------------
def main():
    print(Fore.GREEN + "🤖 Welcome to AI Summarizer!")

    # Ask for user name
    user_name = input("Enter your name: ").strip() or "User"
    print(Fore.YELLOW + f"Hello, {user_name} 👋")

    # Ask for input text
    text = input("\nEnter the text you want to summarize:\n").strip()
    if not text:
        print(Fore.RED + "❌ No input text provided. Exiting...")
        return

    # Ask for optional model
    model_name = input(f"\nEnter model name (or press Enter to use default '{DEFAULT_MODEL}'): ").strip()
    if not model_name:
        model_name = DEFAULT_MODEL

    # Choose summarization style
    print(Fore.MAGENTA + "\nChoose summarization style:")
    print("1️⃣  Standard Summary (Concise)")
    print("2️⃣  Enhanced Summary (Detailed)")

    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        min_len, max_len = 20, 60
    elif choice == "2":
        min_len, max_len = 50, 150
    else:
        print(Fore.RED + "❌ Invalid choice. Defaulting to Standard Summary.")
        min_len, max_len = 20, 60

    # Generate summary
    summary = summarize_text(text, min_len, max_len, model_name)

    if summary:
        print(Fore.GREEN + "\n✅ Summary Generated:")
        print(Fore.WHITE + Style.BRIGHT + summary)
    else:
        print(Fore.RED + "❌ Failed to generate summary.")


if __name__ == "__main__":
    main()
