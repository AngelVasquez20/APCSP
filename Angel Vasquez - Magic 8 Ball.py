import random
import sys
import time
answers = ["Yes", "No", "Maybe", "Not Sure", "Possibly", "Ask Later", "Try Again"]
print("This program is just like Magic 8 Ball. Ask a question and the 8 ball will answer it.")
time.sleep(2)
print("")
print("To end the program enter q, or quit")


def eight_ball():
    yes = 0
    question = input("Please enter in a question")
    while question is not "quit" or question is not "q":
        if question == "q" or "quit":
            sys.exit(0)
        question = random.choice(answers)
        print(question + " " + answers)

eight_ball()