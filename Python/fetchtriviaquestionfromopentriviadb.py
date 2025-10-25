import requests
import random
import html

# Step 1: Fetch trivia questions from Open Trivia DB
url = "https://opentdb.com/api.php?amount=5&type=multiple"
response = requests.get(url)

# Convert JSON to dictionary
data = response.json()

# Extract questions
questions = data["results"]

score = 0

print("\n🎯 Welcome to the Trivia Quiz! 🎯\n")

# Step 2: Loop through questions
for i, q in enumerate(questions, 1):
    question = html.unescape(q["question"])
    correct_answer = html.unescape(q["correct_answer"])
    options = [html.unescape(ans) for ans in q["incorrect_answers"]]
    options.append(correct_answer)
    
    # Shuffle options
    random.shuffle(options)
    
    # Step 3: Display the question
    print(f"Q{i}. {question}")
    for idx, option in enumerate(options, start=1):
        print(f"   {idx}. {option}")
    
    # Step 4: Take user input
    try:
        answer = int(input("Your answer (1-4): "))
        if options[answer-1] == correct_answer:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {correct_answer}\n")
    except:
        print(f"Invalid input! Skipping... Correct answer was {correct_answer}\n")

# Step 5: Show final score
print(f"🎉 Quiz Over! Your final score: {score}/{len(questions)}")
