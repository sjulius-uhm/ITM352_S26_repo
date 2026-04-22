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


@app.route("/")
def home():
    """Start a new quiz."""
    questions = load_questions("questions.json")
    selected_questions = prepare_questions(questions, NUM_QUESTIONS_PER_QUIZ)

    session["questions"] = selected_questions
    session["question_num"] = 0
    session["score"] = 0

    return render_template("index.html")


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    """Show quiz questions and process answers."""
    if "questions" not in session:
        return redirect(url_for("home"))

    questions = session["questions"]
    question_num = session["question_num"]

    if request.method == "POST":
        user_answer = request.form.get("answer")

        question, alternatives = questions[question_num]
        correct_answer = alternatives[0]

        if user_answer == correct_answer:
            session["score"] += 1

        session["question_num"] += 1
        question_num = session["question_num"]

        if question_num >= len(questions):
            return redirect(url_for("result"))

    question, alternatives = questions[session["question_num"]]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))

    return render_template(
        "quiz.html",
        question_num=session["question_num"] + 1,
        total_questions=len(questions),
        question=question,
        options=ordered_alternatives
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