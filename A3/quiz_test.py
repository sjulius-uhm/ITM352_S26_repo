# This test file was created with the help of AI.
# AI was used to generate example test cases for the Flask application.
# I reviewed and adjusted the tests to match my routes, session structure,
# and quiz functionality. I understand what each test is verifying.

import unittest
from unittest.mock import patch
import quiz_webapp

print("\nRunning Quiz Web Application Tests...\n")


class QuizAppTest(unittest.TestCase):
    """Basic tests for the Flask quiz web application."""

    def setUp(self):
        # Set app to testing mode and create a test client
        quiz_webapp.app.config["TESTING"] = True
        self.client = quiz_webapp.app.test_client()

    def test_home_page_loads(self):
        # Test that the home page route ("/") loads successfully
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        print("✓ Home page loads successfully (status 200)")

    def test_quiz_redirects_without_session(self):
        # Test that accessing /quiz without a session redirects to home
        response = self.client.get("/quiz")
        self.assertEqual(response.status_code, 302)
        print("✓ /quiz correctly redirects if no session exists")

    def test_start_regular_quiz(self):
        # Test starting the quiz in regular mode
        response = self.client.post("/start", data={"mode": "regular"}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        print("✓ Regular quiz starts and displays question page")

    def test_start_timed_quiz(self):
        # Test starting the quiz in timed mode and displaying timer
        response = self.client.post("/start", data={"mode": "timed"}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        print("✓ Timed quiz starts and displays timer")

    def test_feedback_page_loads_with_session_data(self):
        # Manually create session data to simulate answering a question
        with self.client.session_transaction() as sess:
            sess["questions"] = [["Test Question", ["A", "B", "C", "D"]]]
            sess["question_num"] = 0
            sess["score"] = 1
            sess["last_result"] = "correct"
            sess["last_question"] = "Test Question"
            sess["last_correct_answer"] = "A"
            sess["last_user_answer"] = "A"
            sess["quiz_timed_out"] = False

        # Test that feedback page loads with this session data
        response = self.client.get("/feedback")
        self.assertEqual(response.status_code, 200)
        print("✓ Feedback page loads correctly with session data")

    @patch("quiz_webapp.save_scores")
    @patch("quiz_webapp.load_scores", return_value=[])
    def test_result_page_loads(self, mock_load_scores, mock_save_scores):
        # Mock score loading/saving so test does not write to file
        with self.client.session_transaction() as sess:
            sess["questions"] = [["Test Question", ["A", "B", "C", "D"]]]
            sess["score"] = 1
            sess["quiz_start_time"] = 0
            sess["missed_questions"] = []
            sess["quiz_timed_out"] = False

        # Test that result page loads and triggers score saving
        response = self.client.get("/result")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(mock_save_scores.called)
        print("✓ Result page loads and score is saved")

    def test_api_questions_returns_json(self):
        # Add questions to session to simulate active quiz
        with self.client.session_transaction() as sess:
            sess["questions"] = [["Test Question", ["A", "B", "C", "D"]]]

        # Test that API returns JSON response
        response = self.client.get("/api/questions")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.is_json)
        print("✓ API /api/questions returns JSON data")

    @patch("quiz_webapp.save_scores")
    @patch("quiz_webapp.load_scores", return_value=[])
    def test_api_score_post(self, mock_load_scores, mock_save_scores):
        # Send test JSON data to score API
        response = self.client.post(
            "/api/score",
            json={"score": 4, "total_questions": 5, "timed_mode": False}
        )

        # Verify response and that score-saving function was called
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.is_json)
        self.assertTrue(mock_save_scores.called)
        print("✓ API /api/score saves score successfully")

    def test_api_scores_returns_json(self):
        # Mock stored scores and test retrieval
        with patch("quiz_webapp.load_scores", return_value=[{"score": 4, "total_questions": 5}]):
            response = self.client.get("/api/scores")
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.is_json)

        print("✓ API /api/scores returns stored scores")


if __name__ == "__main__":
    # Run tests in verbose mode for detailed output
    unittest.main(verbosity=2)