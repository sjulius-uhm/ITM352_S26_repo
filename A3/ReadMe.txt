Quiz Web Application – Assignment 3
Name: Samantha Julius
Date: April 2026

--------------------------------------------------
Project Description
--------------------------------------------------
This project is a Flask-based web quiz application built from my Assignment 1 quiz program. The application allows users to take a quiz using questions loaded from a JSON file. The quiz supports both a regular mode and a timed mode, includes a 50/50 feature, provides feedback after each question, and displays a final results page with detailed performance information.

--------------------------------------------------
Setup Instructions
--------------------------------------------------
1. Make sure Python 3 is installed on your computer.

2. Install Flask if it is not already installed:
   pip install flask

3. Make sure the project folder is structured as follows:

   A3/
       quiz_webapp.py
       questions.json
       scores.json
       static/
           style.css
       templates/
           index.html
           quiz.html
           feedback.html
           result.html

4. Run the application:
   python3 quiz_webapp.py

5. Open a browser and go to:
   http://127.0.0.1:5000

--------------------------------------------------
Usage Guide
--------------------------------------------------
1. On the home page, choose between:
   - Regular Quiz
   - Timed Quiz

2. Answer each question by selecting one option and clicking "Submit Answer."

3. If available, use the 50/50 button once per quiz to remove two incorrect answers.

4. In timed mode:
   - A countdown timer is displayed
   - If time runs out, the question is automatically submitted as a timeout

5. After each question, a feedback page will show:
   - whether the answer was correct, incorrect, or timed out
   - the correct answer
   - current score

6. At the end of the quiz, the results page displays:
   - final score
   - number of correct answers
   - number of incorrect answers
   - total time taken
   - improvement message based on missed questions

--------------------------------------------------
Design Choices
--------------------------------------------------
- Flask Framework:
  Flask was used because it is simple and allows easy handling of routes, templates, and sessions.

- JSON Data Storage:
  Questions are stored in a JSON file so they can be easily modified without changing the code.

- Session-Based Tracking:
  Flask sessions are used to track:
  - current question
  - score
  - quiz mode (timed or regular)
  - 50/50 usage
  - missed questions

  This replaces the global variables used in Assignment 1.

- Randomization:
  Questions and answer choices are randomized for each quiz session to ensure variety.

- Timer Feature:
  A timer was added for timed mode using JavaScript to count down and automatically submit answers.

- 50/50 Feature:
  This feature removes two incorrect answers and can only be used once per quiz.

- Mobile Responsiveness:
  The application was designed to work on both desktop and mobile devices. Responsive CSS was used, and the app was tested on a phone to ensure usability.

- CSS Styling:
  A separate CSS file was used to keep styling separate from HTML, improving readability and maintainability.

- API Routes:
  Basic API routes were added to:
  - retrieve questions
  - store scores
  - view stored scores

--------------------------------------------------
Files Overview
--------------------------------------------------
quiz_webapp.py
Main Flask application containing all quiz logic and routes.

questions.json
Stores quiz questions and answer choices.

scores.json
Stores user quiz results.

templates/
Contains HTML pages for the application:
- index.html (home page)
- quiz.html (question page)
- feedback.html (answer feedback page)
- result.html (final results page)

static/style.css
Contains styling for all pages.

--------------------------------------------------
Notes
--------------------------------------------------
- The application includes basic error handling for missing or invalid JSON files.
- The quiz prevents users from accessing pages out of order.
- Scores are saved after each quiz attempt.
- The application was tested on both desktop and mobile to ensure a responsive layout.