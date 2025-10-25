# random_joke.py
import requests

def get_random_joke() -> str:
    """
    Fetch a random joke from the Official Joke API and return it as a single string.
    Returns a friendly error message if something goes wrong.
    """
    url = "https://official-joke-api.appspot.com/random_joke"#
    try:#test
        response = requests.get(url, timeout=5)     # network call
        response.raise_for_status()                  # raise for HTTP errors (4xx/5xx)
    except requests.RequestException as e:#error
        return f"Error fetching joke: {e}"

    try:
        data = response.json()                       # parse JSON response
    except ValueError:
        return "Error: response was not valid JSON."

    # safe access in case API structure changes
    setup = data.get("setup")
    punchline = data.get("punchline")
    if setup and punchline:
        return f"{setup} — {punchline}"#nested JSon
    else:
        return "Error: unexpected JSON structure from API."

def main():
    print("Welcome to the Random Joke Generator!")
    print("Press Enter to get a new joke, or type 'q' / 'exit' to quit.")

    while True:#true
        user_input = input("> ").strip().lower()
        if user_input in ("q", "exit"):
            print("Goodbye! 😄")
            break

        joke = get_random_joke()#calling my function again
        print("\n" + joke + "\n")

if __name__ == "__main__":#main class
    main()
