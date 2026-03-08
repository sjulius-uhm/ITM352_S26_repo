import quiz

print("TEST 1: Loading questions")
print("--------------------------")
questions = quiz.QUESTIONS
print("Questions loaded:", len(questions))
print()

print("TEST 2: Random question selection")
print("---------------------------------")
selected = quiz.prepare_questions(questions, 3)
print("Selected questions:", selected)
print()

print("TEST 3: 50/50 feature")
print("---------------------")
alternatives = ["Correct", "Wrong1", "Wrong2", "Wrong3"]
result = quiz.use_fifty_fifty(alternatives, "Correct")
print("Original:", alternatives)
print("After 50/50:", result)
print()

print("TEST COMPLETE")