import requests#get http request in python

# Technology category fact endpoint define url API
url = "https://uselessfacts.jsph.pl/category/Technology.json?language=en"
#transalte the data in nhuman readable format 
#json parse response response.json()
#{"text":"HI how are you"
#
#}
#accessing data response.json() print(['text'])
#nested json
#interactive system GUI interactive button click
#1. install request 2. fetch the fact random or number 3. display parse json response

# Function to fetch and display a random technology-related fact
def get_random_technology_fact():# def function() called and used again and again
    response = requests.get(url)#url API
    if response.status_code == 200:# succeddful
        fact_data = response.json()#python dict
        print(f"Did you know? {fact_data['text']}")#json response
    else:
        print("Failed to fetch fact")#false

# Main loop to interact with the user
while True:# condtion while condition stmt
    user_input = input("Press Enter to get a random technology fact or type 'q' to quit...")
    if user_input.lower() == 'q':#.lower case or .upper
        break
    get_random_technology_fact()
