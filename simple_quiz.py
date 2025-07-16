questions = [
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "What color is the sky?", "answer": "blue"}
]

def ask_question(q):
    user_answer = input(q["question"] + " ")
    if user_answer.lower() == q["answer"].lower():
        print("Correct ✅")
    else:
        print("Wrong ❌")

ask_question(questions[0])
ask_question(questions[1])