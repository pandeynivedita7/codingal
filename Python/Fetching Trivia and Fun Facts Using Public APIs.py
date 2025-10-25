import requests # http get request API
import random #shuffling
import html #used to decode HTML

# Education-focused categories (General Knowledge, Science, History, etc.)
EDUCATION_CATEGORY_ID = 8  # General Knowledge category (most educational)
API_URL = f"https://opentdb.com/api.php?amount=10&category={EDUCATION_CATEGORY_ID}&type=multiple"#URL

def get_education_questions():# def fun numa():
    response = requests.get(API_URL)
    if response.status_code == 200:# ok respone
        data = response.json()# java script object notation
        if data['response_code'] == 0 and data['results']:
            return data['results']
    return None

def run_quiz():
    questions = get_education_questions()
    if not questions:# not opening invaild
        print("Failed to fetch educational questions")
        return

    score = 0
    print("Welcome to the Education Quiz!\n")

    for i, q in enumerate(questions, 1):# loop of 10
        # Decode HTML entities and prepare options
        question = html.unescape(q['question'])
        correct = html.unescape(q['correct_answer'])
        incorrects = [html.unescape(a) for a in q['incorrect_answers']]

        # Create and shuffle options
        options = incorrects + [correct]
        random.shuffle(options)

        # Display question
        print(f"Question {i}: {question}")
        for idx, option in enumerate(options, 1):
            print(f"  {idx}. {option}")

        # Get and validate answer
        while True:#loop 
            try:#correct statemt
                choice = int(input("\nYour answer (1-4): "))
                if 1 <= choice <= 4:
                    break
            except ValueError:# wrong you go here
                pass
            print("Invalid input! Please enter 1-4")

        # Check answer
        if options[choice-1] == correct:
            print("✓ Correct!\n")
            score += 1# score=score+1 score+=1
        else:
            print(f"✗ Wrong! Correct answer: {correct}\n")

    print(f"Final Score: {score}/{len(questions)}")#question string number len()number of question
    print(f"Percentage: {score/len(questions)*100:.1f}%")#.1f only i floating point values
# entry point only execute the import once then it use it
if __name__ == "__main__":
    run_quiz()
    #Pulls 10 random General Knowledge questions from an online API.

#Decodes HTML content.

#Shuffles options.

#Accepts user input.

#Displays correctness and keeps a running score.

#Shows final results with a percentage.
