# flashcard_quiz.py
import random

questions = [
    {"question": "What is 5 x 6?", "answer": "30"},
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What language do they speak in Mexico?", "answer": "Spanish"},
    {"question": "What is the square root of 81?", "answer": "9"},
    {"question": "What is 12 divided by 4?", "answer": "3"},
    {"question": "What is the 7th month of the year?", "answer": "July"},
    {"question": "What is the square root of 36", "answer": "6"}
]

score = 0
total_questions = len(questions)  # Ask all questions

def ask_question(q):
    global score
    print(q["question"])
    user_answer = input("Your answer: ")
    if user_answer.strip().lower() == q["answer"].strip().lower():
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong. The correct answer was {q['answer']}.\n")

random.shuffle(questions)

for i in range(total_questions):
    ask_question(questions[i])

percentage = (score / total_questions) * 100
print(f"You got {score} out of {total_questions} correct!\n")
print(f"That's {round(percentage)}%!")