import random
from questions import questions

def regular_quiz():
    while True:

        random.shuffle(questions)

        score = 0

        print("Answer the following questions: ")

        for q in questions:
            answer = input(q[0] + " ").lower()

            if answer == q[1].lower():
                print("Correct!")
                score = score + 1
            else:
                print(f"Incorrect. The correct answer was: {q[1]}")

        print(f"Score: {score}/{len(questions)}")

        print("1. Retry quiz")
        print("2. Back to menu")

        choice = input("Choose: ")

        if choice == "1":
            continue
        elif choice == "2":
            break
        else:
                print("Invalid choice")