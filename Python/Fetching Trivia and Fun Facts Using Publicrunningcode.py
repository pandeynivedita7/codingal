import requests
import random
import html

# General Knowledge category
API_URL = "https://opentdb.com/api.php?amount=5&category=9&type=multiple"

def get_education_questions():
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        if data['response_code'] == 0 and data['results']:
            return data['results']
    return None

def run_quiz(auto_mode=True):
    questions = get_education_questions()
    if not questions:
        print("Failed to fetch educational questions")
        return

    score = 0
    print("Welcome to the Education Quiz!\n")

    for i, q in enumerate(questions, 1):
        question = html.unescape(q['question'])
        correct = html.unescape(q['correct_answer'])
        incorrects = [html.unescape(a) for a in q['incorrect_answers']]

        options = incorrects + [correct]
        random.shuffle(options)

        print(f"Question {i}: {question}")
        for idx, option in enumerate(options, 1):
            print(f"  {idx}. {option}")

        if auto_mode:
            choice = random.randint(1, 4)
            print(f"\nSelected Answer: {choice}. {options[choice-1]}")
        else:
            choice = int(input("\nYour answer (1-4): "))

        if options[choice-1] == correct:
            print("✓ Correct!\n")
            score += 1
        else:
            print(f"✗ Wrong! Correct answer: {correct}\n")

    print(f"Final Score: {score}/{len(questions)}")
    print(f"Percentage: {score/len(questions)*100:.1f}%")

# Run the quiz
run_quiz(auto_mode=True)