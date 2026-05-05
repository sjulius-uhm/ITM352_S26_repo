# Quiz game.  Seventh version.
# Name: Samantha Julius
# Date: Feb. 26, 2026
# Make QUESTIONS a dictionary, to include answer options and the correct choice.
# Allow the user to select the correct answer by its label.
# Improve the look and usability.  Keep track of correct answers. 
# Loop until a user provides a correct alternative.
# Randomize the order of questions and order of the answer alternatives per question
# Refactor the code to use functions

from string import ascii_lowercase
import random

NUM_QUESTIONS_PER_QUIZ = 5

QUESTIONS = {
     "What is the airspeed of an unladen swallow in miles/hr": 
     ["12", "8", "11", "15"],
     "What is the capital of Texas": 
     ["Austin", "San Antonio", "Dallas", "Waco"],
      "The Last Supper was painted by which artist": 
     ["Da Vinci", "Rembrandt", "Picasso", "Michelangelo"],
     "Which classic novel opens with the line “Call Me Ishmael”?":
     ["Moby Dick", "Wuthering Heights", "The Old Man and the Sea", "The Scarlet Letter"]
}

def prepare_questions(questions, num_questions):
    num_questions = min(num_questions, len(questions))
    return random.sample(list(questions.items()), k=num_questions)

def get_answer(question, alternatives):
    print(f"{question}?")
    labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
        print(f"Please answer one of {', '.join(labeled_alternatives)}")

    return labeled_alternatives[answer_label]

def ask_question(question, alternatives):
    correct_answer = alternatives[0]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))

    answer = get_answer(question, ordered_alternatives)
    if answer == correct_answer:
        print("⭐ Correct! ⭐")
        return 1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")
        return 0


# Main quiz steps: preparing questions, running the quiz, giving feedback
questions = prepare_questions(QUESTIONS, num_questions=NUM_QUESTIONS_PER_QUIZ)

# Process (main loop)
num_correct = 0
for num, (question,alternatives) in enumerate(questions,start=1):
    print(f"Question {num}: ")
    num_correct += ask_question(question,alternatives)

# Postprocess
print(f"\nYou got {num_correct} correct. Thank you for playing!")