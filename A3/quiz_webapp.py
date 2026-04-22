# Name: Samantha Julius
# Date: April 21, 2026

# Flask imports for web app functionality
from flask import Flask, redirect, render_template, request, session, url_for, jsonify
import random
import json
import time

app = Flask(__name__)
app.secret_key = "my_quiz_key"   # required for session tracking

# Quiz configuration
NUM_QUESTIONS_PER_QUIZ = 5
QUESTION_TIME_LIMIT = 10   # seconds per question (timed mode)


def load_questions(filename):  #copied Json from A1
    """Load questions from the JSON file with basic error handling."""
    try:
        with open(filename) as f:
            questions = json.load(f)
        return questions
    except FileNotFoundError:
        print("Error: questions file not found.")  # requirement 7: error handling and validation
        return {}
    except json.JSONDecodeError:
        print("Error: JSON file is not formatted correctly.")
        return {}


def prepare_questions(questions, num_questions):  # Ensures each quiz session is different.
    """
    Select a random subset of questions for the quiz.
    Similar to Assignment 1 logic but adapted for web use.
    """
    num_questions = min(num_questions, len(questions))
    selected = random.sample(list(questions.items()), k=num_questions)
    return [[question, alternatives] for question, alternatives in selected]


def use_fifty_fifty(alternatives, correct_answer):  # requirement from A1
    """
    Custom feature: remove two incorrect answers.
    Keeps the correct answer and one random wrong answer.
    """
    wrong_answers = [choice for choice in alternatives if choice != correct_answer]
    kept_wrong_answer = random.choice(wrong_answers)
    reduced_alternatives = [correct_answer, kept_wrong_answer]

    # shuffle remaining answers
    return random.sample(reduced_alternatives, k=len(reduced_alternatives))


def get_improvement_message(missed_questions):
    """
    Generate a simple improvement message based on missed questions.
    This is a custom feature added for detailed feedback.
    """
    if len(missed_questions) == 0:
        return "Great job. You answered every question correctly."

    missed_text = " ".join(missed_questions).lower()

    messages = []

    if "hawaii" in missed_text:
        messages.append("Review your Hawaii knowledge.")

    if "python" in missed_text or "itm" in missed_text:
        messages.append("Revisit class material and Python concepts.")

    if len(messages) == 0:
        return "Review the questions you missed."

    return " ".join(messages)

#  confused on requirement: " Store questions, answer choices, and USER SCORE DATA in JSON format or a simple data file. Use server-side Python code to handle data storage and retrieval."
def load_scores(filename):
    """Load saved scores from JSON file."""
    try:
        with open(filename) as f:
            return json.load(f)
    except FileNotFoundError:
        return []


# but added it to make sure requirements are fulfilled. it just keeps adding every test score
def save_scores(filename, scores):
    """Save updated score list to JSON file."""
    with open(filename, "w") as f:
        json.dump(scores, f, indent=4)


@app.route("/")
def home():  # removed -> type hint to improve readability and documentation. possibly got an error i cant remember
    """Display home page."""
    return render_template("index.html")


@app.route("/start", methods=["POST"])
def start_quiz():
    """
    Initialize a new quiz session.
    This replaces Assignment 1's main() setup logic.
    """
    mode = request.form.get("mode")

    questions = load_questions("questions.json")

    # Validation: prevent starting quiz if no questions. requirement 7
    if len(questions) == 0:
        return render_template("index.html", error="No questions available.")

    selected_questions = prepare_questions(questions, NUM_QUESTIONS_PER_QUIZ)

    # Store quiz state in session (replaces global variables from A1)
    session["questions"] = selected_questions
    session["question_num"] = 0
    session["score"] = 0
    session["fifty_fifty_used"] = False
    session["quiz_timed_out"] = False
    session["timed_mode"] = (mode == "timed")
    session["missed_questions"] = []

    # Track total quiz time
    session["quiz_start_time"] = time.time()

    # Clear any previous session data
    session.pop("reduced_options", None)
    session.pop("last_result", None)
    session.pop("question_start_time", None)

    return redirect(url_for("quiz"))


# main quiz controller
@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    """
    Main quiz logic:
    - displays question
    - handles answer submission
    - handles 50/50 feature
    - handles timer logic
    """
    if "questions" not in session:
        return redirect(url_for("home"))

    questions = session["questions"]
    question_num = session["question_num"]

    question, alternatives = questions[question_num]
    correct_answer = alternatives[0]

    timed_mode = session.get("timed_mode", False)

    if request.method == "POST":
        action = request.form.get("action")

        # -------- 50/50 FEATURE --------
        if action == "fifty":
            if not session["fifty_fifty_used"] and len(alternatives) == 4:
                session["reduced_options"] = use_fifty_fifty(alternatives, correct_answer)
                session["fifty_fifty_used"] = True

            # keep remaining time if timed
            if timed_mode and "question_start_time" in session:
                elapsed = int(time.time() - session["question_start_time"])
                time_left = max(0, QUESTION_TIME_LIMIT - elapsed)
            else:
                time_left = 0

            return render_template(
                "quiz.html",
                question_num=question_num + 1,
                total_questions=len(questions),
                question=question,
                options=session.get("reduced_options", alternatives),
                can_use_fifty=(len(alternatives) == 4 and not session["fifty_fifty_used"]),
                error="",
                time_limit=time_left if timed_mode else 0,
                timed_mode=timed_mode
            )

        # -------- ANSWER SUBMISSION --------
        elif action == "submit":
            user_answer = request.form.get("answer")
            timed_out = request.form.get("timed_out", "false")

            # calculate elapsed time for timed mode
            if timed_mode and "question_start_time" in session:
                elapsed = int(time.time() - session["question_start_time"])
            else:
                elapsed = 0

            # -------- TIMER LOGIC --------
            if timed_mode and (timed_out == "true" or elapsed >= QUESTION_TIME_LIMIT):
                session["last_result"] = "timeout"
                session["quiz_timed_out"] = True
                session["missed_questions"].append(question)
                return redirect(url_for("feedback"))

            # validation: no answer selected
            if user_answer is None:
                return render_template(
                    "quiz.html",
                    question_num=question_num + 1,
                    total_questions=len(questions),
                    question=question,
                    options=random.sample(alternatives, k=len(alternatives)),
                    can_use_fifty=True,
                    error="Please select an answer.",
                    time_limit=QUESTION_TIME_LIMIT if timed_mode else 0,
                    timed_mode=timed_mode
                )

            # check answer correctness
            if user_answer == correct_answer:
                session["score"] += 1
                session["last_result"] = "correct"
            else:
                session["last_result"] = "incorrect"
                session["missed_questions"].append(question)

            return redirect(url_for("feedback"))

    # -------- DISPLAY QUESTION --------
    options = random.sample(alternatives, k=len(alternatives))

    # start timer for each question (timed mode only)
    if timed_mode:
        session["question_start_time"] = time.time()

    return render_template(
        "quiz.html",
        question_num=question_num + 1,
        total_questions=len(questions),
        question=question,
        options=options,
        can_use_fifty=(len(alternatives) == 4 and not session["fifty_fifty_used"]),
        error="",
        time_limit=QUESTION_TIME_LIMIT if timed_mode else 0,
        timed_mode=timed_mode
    )


# feedback page after each question
@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    """Display feedback for the previous question."""
    if "last_result" not in session:
        return redirect(url_for("quiz"))

    if request.method == "POST":
        # if timed quiz ended, go straight to result
        if session.get("quiz_timed_out", False):
            return redirect(url_for("result"))

        session["question_num"] += 1

        # check if quiz is finished
        if session["question_num"] >= len(session["questions"]):
            return redirect(url_for("result"))

        return redirect(url_for("quiz"))

    return render_template(
        "feedback.html",
        result=session["last_result"],
        score=session["score"]
    )


@app.route("/result")
def result():
    """Display final results and save score."""
    if "questions" not in session:
        return redirect(url_for("home"))

    score = session["score"]
    total_questions = len(session["questions"])

    num_correct = score
    num_incorrect = total_questions - score

    total_time = int(time.time() - session["quiz_start_time"])

    improvement_message = get_improvement_message(session.get("missed_questions", []))

    # -------- SAVE SCORE --------
    scores = load_scores("scores.json")
    scores.append({
        "score": score,
        "total_questions": total_questions,
        "time": total_time
    })
    save_scores("scores.json", scores)

    return render_template(
        "result.html",
        score=score,
        total_questions=total_questions,
        num_correct=num_correct,
        num_incorrect=num_incorrect,
        total_time=total_time,
        improvement_message=improvement_message
    )


# -------- API ROUTES --------

@app.route("/api/questions")
def api_questions():
    """Return current quiz questions as JSON."""
    return jsonify(session.get("questions", []))


@app.route("/api/score", methods=["POST"])
def api_score():
    """Store score via API."""
    data = request.get_json()

    scores = load_scores("scores.json")
    scores.append(data)
    save_scores("scores.json", scores)

    return jsonify({"message": "Score saved"})


@app.route("/api/scores")
def api_scores():
    """Return all stored scores."""
    return jsonify(load_scores("scores.json"))


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()