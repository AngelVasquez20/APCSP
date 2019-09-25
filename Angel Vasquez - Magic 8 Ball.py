import time
import random

answers = ["maybe", "not sure", "could be", "positive", "ask again", "Yes", "no", "Possibly", "Ask later", "I'm tired"
    , "I don't know", "YESSS", "I think you are"]


def eight_ball():
    track = 0
    while True:
        name = input("What is your name:")
        print("Welcome to Magic 8 Ball %s where you ask a question and the magic ball will answer it for you." % name)
        time.sleep(2)
        print("")
        print("%s To end the game you can enter q or quit" % name)
        question = input("Type a question to shake the magic 8 ball %s: " % name)
        print("")
        if question == "q" or question == "quit":
            print("you have shake the magic ball %d times. Thanks for playing" % track)
            return False
        for i in range(0, 11):
            print('Shaking...')
            print("")
            time.sleep(1)
            print(random.choice(answers))
            time.sleep(1)
            break


eight_ball()
