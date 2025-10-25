import requests

# -------------------------------
# 1. Dog API Example
# -------------------------------
def fetch_random_dog_images(count=5):
    print("\n🐶 Fetching Random Dog Images...")
    for i in range(count):
        response = requests.get("https://dog.ceo/api/breepids/image/random")
        if response.status_code == 200:
            data = response.json()
            print(f"Dog {i+1}: {data['message']}")
        else:
            print("Error fetching dog image.")


# -------------------------------
# 2. JSONPlaceholder Example
# -------------------------------
def fetch_posts(limit=5):
    print("\n📝 Fetching Posts from JSONPlaceholder...")
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        posts = response.json()
        for post in posts[:limit]:
            print(f"Post ID: {post['id']}, Title: {post['title']}")
    else:
        print("Error fetching posts.")


# -------------------------------
# 3. Pokémon API Example
# -------------------------------
def fetch_pokemon_info(pokemon_name="pikachu"):
    print(f"\n⚡ Fetching Pokémon Info for '{pokemon_name}'...")
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print("Name:", data["name"].title())
        print("Height:", data["height"])
        print("Weight:", data["weight"])
        abilities = [ability["ability"]["name"] for ability in data["abilities"]]
        print("Abilities:", ", ".join(abilities))
    else:
        print("Pokémon not found!")


# -------------------------------
# MAIN PROGRAM
# -------------------------------
if __name__ == "__main__":
    print("📌 Exploring Public APIs and Understanding JSON Data")
    print("---------------------------------------------------")

    # Task 1: Fetch random dog images
    fetch_random_dog_images()

    # Task 2: Fetch some posts
    fetch_posts(limit=5)

    # Task 3: Fetch Pokémon info (user input)
    pokemon = input("\nEnter a Pokémon name (e.g., pikachu, charizard, bulbasaur): ")
    fetch_pokemon_info(pokemon)
