import json

filename = "quiz_data.json"

with open(filename, "r") as jsonfile:
    QUESTIONS = json.load(jsonfile)

for question, choices in QUESTIONS.items():
    print(question)
    for choice in choices:
        print(f"  - {choice}")
    print()  