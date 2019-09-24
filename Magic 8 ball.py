import random
import time
answers = ["Yes", "No", "Maybe", "Not Sure", "Possibly", "Ask Later", "Try Again", "Could be", "Im tired", "Im tired"]


def eight_ball():
    while True:
        print("")
        print("Welcome To Magic 8 Ball where you type in a question and get a response back.")
        time.sleep(1)
        print("")
        press_play = input("To began please enter play")
        if press_play == "play".lower():
            print("Loading...")
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
            time.sleep(1)
            print("")
            print("To end or quit you can put q, exit, or quit")
            question = input("type in a question")
            print("")
            if question == "q" or "exit" or "quit":
                return
            answer = random.choice(answers)
            print(answer)



eight_ball()
