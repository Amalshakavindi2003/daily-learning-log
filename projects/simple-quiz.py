score = 0

questions = [
    {"question": "What does HTML stand for?",
     "answer": "hypertext markup language"},
    {"question": "What does CSS stand for?",
     "answer": "cascading style sheets"},
    {"question": "What does Git stand for?",
     "answer": "global information tracker"},
    {"question": "What is Python?",
     "answer": "programming language"},
    {"question": "What does SQL stand for?",
     "answer": "structured query language"}
]

print("Welcome to the Quiz!")
print("--------------------")

for i, q in enumerate(questions, 1):
    print(f"\nQuestion {i}: {q['question']}")
    answer = input("Your answer: ").lower().strip()
    if answer == q["answer"]:
        print("Correct! ✓")
        score += 1
    else:
        print(f"Wrong! The answer is: {q['answer']}")

print(f"\nYour Score: {score}/{len(questions)}")