import requests
from config import HF_API_KEY
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Default model
DEFAULT_MODEL = "facebook/bart-large-cnn"


# Correct Router API URL
def build_api_url(model_name):

    return f"https://router.huggingface.co/hf-inference/models/{model_name}"


# API call function
def query(payload, model_name):

    api_url = build_api_url(model_name)

    headers = {

        "Authorization": f"Bearer {HF_API_KEY}",

        "Content-Type": "application/json"

    }

    try:

        response = requests.post(

            api_url,

            headers=headers,

            json=payload,

            timeout=60

        )

        print(Fore.CYAN + f"\nStatus Code: {response.status_code}")

        # Handle error
        if response.status_code != 200:

            print(Fore.RED + "API Error:")
            print(response.text)
            return None

        # Handle empty response
        if not response.text.strip():

            print(Fore.RED + "Empty response")
            return None

        return response.json()

    except requests.exceptions.Timeout:

        print(Fore.RED + "Request Timeout")
        return None

    except requests.exceptions.RequestException as e:

        print(Fore.RED + f"Request Failed: {e}")
        return None

    except Exception as e:

        print(Fore.RED + f"Error: {e}")
        return None


# Summarization function
def summarize_text(text, min_length, max_length, model_name):

    payload = {

        "inputs": text,

        "parameters": {

            "min_length": min_length,

            "max_length": max_length

        }
    }

    print(Fore.BLUE + Style.BRIGHT +
          f"\nUsing Model: {model_name}")

    result = query(payload, model_name)

    if result and isinstance(result, list):

        if "summary_text" in result[0]:

            return result[0]["summary_text"]

    print(Fore.RED + "Invalid response format")
    print(result)

    return None


# Main function
def main():

    print(Fore.YELLOW + Style.BRIGHT +
          "\n===== AI TEXT SUMMARIZER =====")

    name = input("\nEnter your name: ").strip()

    if not name:

        name = "User"

    print(Fore.GREEN + f"\nWelcome {name}")


    text = input(
        Fore.YELLOW +
        "\nEnter text to summarize:\n> "
    ).strip()

    if not text:

        print(Fore.RED + "No text entered")
        return


    model = input(

        Fore.YELLOW +

        "\nEnter model name"

        "\nPress Enter for default: "

    ).strip()


    if not model:

        model = DEFAULT_MODEL


    print(Fore.YELLOW +

          "\nChoose Summary Style")

    print("1. Standard")

    print("2. Detailed")

    choice = input("Enter choice: ").strip()


    if choice == "2":

        min_length = 80

        max_length = 200

    else:

        min_length = 30

        max_length = 120


    summary = summarize_text(

        text,

        min_length,

        max_length,

        model

    )


    if summary:

        print(Fore.GREEN + Style.BRIGHT +

              f"\nSummary for {name}:\n")

        print(summary)

    else:

        print(Fore.RED +

              "\nFailed to generate summary")


# Run program
if __name__ == "__main__":

    main()