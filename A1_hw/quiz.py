# Quiz game. Assignment version
# Name: Samantha Julius
# Date: March 7, 2026
# Allow the user to select the correct answer by its label.
# Improve the look and usability. Keep track of correct answers.
# Randomize the order of questions and order of the answer alternatives per question.
# Refactor the code to use functions.
# Put the questions into a JSON file and read from it.
# Allow for different numbers of answer alternatives per question.
# Add a one-time 50/50 feature that removes two incorrect answers from a question with 4 answer choices.

from string import ascii_lowercase
import random
import json

# Read in and load the file of quiz questions
f = open('questions.json')
NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS = json.load(f)

# Functions for main processing steps
def prepare_questions(questions, num_questions):
    num_questions = min(num_questions, len(questions))
    return random.sample(list(questions.items()), k=num_questions)

def use_fifty_fifty(alternatives, correct_answer):
    wrong_answers = [choice for choice in alternatives if choice != correct_answer]
    kept_wrong_answer = random.choice(wrong_answers)
    reduced_alternatives = [correct_answer, kept_wrong_answer]
    return random.sample(reduced_alternatives, k=len(reduced_alternatives))

def get_answer(question, alternatives, fifty_fifty_available):
    correct_answer = alternatives[0]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))
    while True:
        print(question)
        labeled_alternatives = dict(zip(ascii_lowercase, ordered_alternatives))
        for label, alternative in labeled_alternatives.items():
            print(f"  {label}) {alternative}")

        if fifty_fifty_available and len(ordered_alternatives) == 4:
            print("  Type 50 to use your one-time 50/50 lifeline.")
            
        answer_label = input("\nChoice? ").strip().lower()
        if answer_label == "50":
            if not fifty_fifty_available:
                print("You have already used the 50/50 lifeline.\n")
            elif len(ordered_alternatives) != 4:
                print("50/50 can only be used on questions with exactly 4 answer choices.\n")
            else:
                ordered_alternatives = use_fifty_fifty(ordered_alternatives, correct_answer)
                fifty_fifty_available = False
                print("50/50 used. Two wrong answers were removed.\n")
            continue

        if answer_label in labeled_alternatives:
            return labeled_alternatives[answer_label], fifty_fifty_available
        
        print(f"Please answer one of {', '.join(labeled_alternatives)}.\n")

def ask_question(question, alternatives, fifty_fifty_available):
    correct_answer = alternatives[0]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))
    
    answer, fifty_fifty_available = get_answer(question, ordered_alternatives, fifty_fifty_available)
    if answer == correct_answer:
        print("⭐ Correct! ⭐\n")
        return 1, fifty_fifty_available
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}\n")
        return 0, fifty_fifty_available

# Main quiz steps: preparing questions, running the quiz, giving feedback
questions = prepare_questions(QUESTIONS, num_questions=NUM_QUESTIONS_PER_QUIZ)

# Process (main loop)
num_correct = 0
fifty_fifty_available = True

print("Welcome to my Quiz!")
print("Answer by typing the letter of your choice.")
print("Once per game, you may type 50 to remove two wrong answers from a question with 4 choices.\n")

for num, (question, alternatives) in enumerate(questions, start=1):
    print(f"Question {num}:")
    score, fifty_fifty_available = ask_question(question, alternatives, fifty_fifty_available)
    num_correct += score

# Postprocess
print(f"\nYou got {num_correct} correct. Thank you for playing!")