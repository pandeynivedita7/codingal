import os
import time
from google import genai
from google.genai import types
import config  # Assuming you have an API key stored in config.py

# To run this code, install the required dependency:
# pip install google-genai

def generate_response(prompt, temperature=0.5):
    """Generate a response from Gemini API with a specified temperature."""
    try:
        client = genai.Client(api_key=config.GEMINI_API_KEY)  # Load your API key
        response = client.models.generate_content(
            model="gemini-1.5-flash",  # or gemini-1.5-pro depending on your need
            contents=prompt,
            config=types.GenerationConfig(
                temperature=temperature
            )
        )
        return response.text
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    prompt = input("Enter your prompt: ")

    print("\n--- Response with Low Temperature (0.2) ---")
    print(generate_response(prompt, temperature=0.2))

    time.sleep(2)

    print("\n--- Response with Medium Temperature (0.5) ---")
    print(generate_response(prompt, temperature=0.5))

    time.sleep(2)

    print("\n--- Response with High Temperature (0.9) ---")
    print(generate_response(prompt, temperature=0.9))
