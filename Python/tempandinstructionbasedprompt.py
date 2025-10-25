import os
import time
import json
from google import genai
from google.genai import types
import config  # Make sure this contains GEMINI_API_KEY = "your_api_key_here"

# To run this code, first install:
# pip install google-genai

def generate_response(prompt, temperature=0.5, retries=3):
    """
    Generate a response from Gemini API with a specified temperature.
    Retries automatically if quota/rate limits are hit.
    """
    for attempt in range(1, retries + 1):
        try:
            # Initialize the Gemini client
            client = genai.Client(api_key=config.GEMINI_API_KEY)

            # Create the content structure
            contents = [
                types.Content(
                    role="user",
                    parts=[types.Part.from_text(text=prompt)],
                ),
            ]

            # Configure generation parameters
            generate_content_config = types.GenerateContentConfig(
                temperature=temperature,
            )

            # Send the prompt to Gemini API
            response = client.models.generate_content(
                model="gemini-1.5-pro",
                contents=contents,
                config=generate_content_config,
            )

            # Return the generated text
            return response.candidates[0].content.parts[0].text

        except Exception as e:
            error_str = str(e)
            print(f"[Attempt {attempt}] Error: {error_str}")

            # Handle RESOURCE_EXHAUSTED (429) errors
            if "RESOURCE_EXHAUSTED" in error_str:
                try:
                    # Parse retryDelay from error JSON if present
                    error_json = json.loads(error_str[error_str.find("{"):])
                    retry_delay_str = error_json['error']['details'][-1].get('retryDelay', '60s')
                    retry_delay = int(retry_delay_str.replace("s", ""))
                except Exception:
                    retry_delay = 60  # Default to 60 seconds

                print(f"Quota hit. Waiting {retry_delay} seconds before retrying...")
                time.sleep(retry_delay)
            else:
                return f"Error generating response: {error_str}"

    return "Failed after multiple retries."


if __name__ == "__main__":
    prompt_text = "Explain AI prompt engineering in simple terms."
    temperature_value = 0.7

    print("Sending request to Gemini API...")
    result = generate_response(prompt_text, temperature=temperature_value)

    print("\n--- Response ---")
    print(result)
