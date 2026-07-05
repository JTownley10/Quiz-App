from quiz import regular_quiz
from multiple_choice import multiple_choice_quiz

while True:
    print("   Computer Science Quiz   ")
    print("1. Regular Quiz")
    print("2. Multiple Choice Questions")

    choice = input("Choose a quiz type: ")

    if choice =="1":
        regular_quiz()
    elif choice =="2":
        multiple_choice_quiz()
    else:
        print("Invalid Option")
