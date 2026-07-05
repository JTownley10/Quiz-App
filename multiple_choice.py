import random
from mc_questions import questions

def multiple_choice_quiz():
    while True:

        random.shuffle(questions)

        score = 0

        print("   Multiple Choice Quiz   ")

        for q in questions:
            print(q["question"])

            print("A.", q["options"][0])
            print("B.", q["options"][1])
            print("C.", q["options"][2])
            print("D.", q["options"][3])

            answer = input("Answer A/B/C/D: ").upper()

            mapping = {"A": 0, "B": 1, "C": 2, "D": 3}

            if answer in mapping and mapping[answer] == q["answer"]:
                print("Correct!")
                score = score + 1
            else:
                correct_letter = ["A", "B", "C", "D"][q["answer"]]
                print(f"Incorrect. Correct answer was {correct_letter}")

        print(f"Final score: {score}/{len(questions)}")

        print("1. Retry quiz")
        print("2. Back to menu")

        choice = input("Choose: ")

        if choice == "1":
            continue
        elif choice == "2":
            break
        else:
            print("Invalid choice")