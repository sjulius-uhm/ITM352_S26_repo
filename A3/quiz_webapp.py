# Name: Samantha Julius
# Date: April 2026

from flask import Flask, redirect, render_template, request, session, url_for
import random
import json

app = Flask(__name__)
app.secret_key = "my_quiz_key"

NUM_QUESTIONS_PER_QUIZ = 5


def load_questions(filename):
    """Load questions from the JSON file."""
    f = open(filename)
    questions = json.load(f)
    f.close()
    return questions


def prepare_questions(questions, num_questions):
    """Select a random set of questions for one quiz."""
    num_questions = min(num_questions, len(questions))
    selected = random.sample(list(questions.items()), k=num_questions)
    return [[question, alternatives] for question, alternatives in selected]


def use_fifty_fifty(alternatives, correct_answer):
    """Remove two wrong answers from a 4-choice question."""
    wrong_answers = [choice for choice in alternatives if choice != correct_answer]
    kept_wrong_answer = random.choice(wrong_answers)
    reduced_alternatives = [correct_answer, kept_wrong_answer]
    return random.sample(reduced_alternatives, k=len(reduced_alternatives))


@app.route("/")
def home():
    """Start a new quiz."""
    questions = load_questions("questions.json")
    selected_questions = prepare_questions(questions, NUM_QUESTIONS_PER_QUIZ)

    session["questions"] = selected_questions
    session["question_num"] = 0
    session["score"] = 0
    session["fifty_fifty_used"] = False

    return render_template("index.html")


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    """Show quiz questions and process answers."""
    if "questions" not in session:
        return redirect(url_for("home"))

    questions = session["questions"]
    question_num = session["question_num"]

    question, alternatives = questions[question_num]
    correct_answer = alternatives[0]

    if request.method == "POST":
        action = request.form.get("action")

        if action == "fifty":
            if not session["fifty_fifty_used"] and len(alternatives) == 4:
                reduced_alternatives = use_fifty_fifty(alternatives, correct_answer)
                session["reduced_options"] = reduced_alternatives
                session["fifty_fifty_used"] = True

        elif action == "submit":
            user_answer = request.form.get("answer")

            if user_answer == correct_answer:
                session["score"] += 1

            session["question_num"] += 1

            if session["question_num"] >= len(questions):
                return redirect(url_for("result"))

            session.pop("reduced_options", None)

            question_num = session["question_num"]
            question, alternatives = questions[question_num]
            correct_answer = alternatives[0]

    if "reduced_options" in session:
        options = session["reduced_options"]
    else:
        options = random.sample(alternatives, k=len(alternatives))

    return render_template(
        "quiz.html",
        question_num=session["question_num"] + 1,
        total_questions=len(questions),
        question=question,
        options=options,
        fifty_fifty_used=session["fifty_fifty_used"],
        can_use_fifty=(len(alternatives) == 4 and not session["fifty_fifty_used"])
    )


@app.route("/result")
def result():
    """Show the final score."""
    if "questions" not in session:
        return redirect(url_for("home"))

    score = session["score"]
    total_questions = len(session["questions"])

    return render_template("result.html", score=score, total_questions=total_questions)


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()