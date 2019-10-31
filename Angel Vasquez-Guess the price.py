import random
import time

numbercost = ["1000", "500", "1000", "1500", "6000", "5000", "400000", "500000", "220", "150", "135", "150", "250",
              "200"]
randomopposcore = ["1", "2", "3", "4", "5", "6"]
randomprize = ["$100,000,000 Dollars", "Lamborghini", "New Apple Iphone 10s max", "New Apple Iphone 11 pro max",
               "100,000 dollars", "5,000,000 dollars", "Macbook Pro", "Flat Screen T.V."]
name = input("To start off what's your name:")
print("%s, you will play a game where you guess the price for things, if you get a higher score than your opponent "
      "you have the chance to win a random good prize. GOOD LUCK! " % name)

time.sleep(1)
print()


def opponetscore():
    # print("Your opponent's score to beat is" + " " + random.choice(randomopposcore))
    opposcore = random.choice(randomopposcore)
    print("Your opponent's score to beat is" + " " + opposcore)
    return opposcore


opposcorebeat = opponetscore()


time.sleep(1)


print()


def guessprice():
    score = 0
    print("We will start")
    time.sleep(0.5)
    guess1stprice = input("How much does an Apple Iphone 10 max cost $1,000 or $500")
    while guess1stprice not in numbercost:
        print("The number you entered isn't an option choose again")
        guess1stprice = input("How much does an Apple Iphone 10 max cost $1,000 or $500")
    if guess1stprice == "1000":
        score += 1
        print("Correct you get one point")
        print("Score =" + " " + str(score))
    if guess1stprice == "500":
        print("Incorrect, sorry no point")
        print("Score =" + " " + str(score))

    guess2ndprice = input("How much does a 60- or 70-inch flat screen T.V. cost $1,000 or $1,500?")
    while guess2ndprice not in numbercost:
        print("The number you enter isn't an option choose again")
        guess2ndprice = input("How much does a 60- or 70-inch flat screen T.V. cost $1,000 or $1,500?")
    if guess2ndprice == "1000":
        score += 1
        print("Correct, 1 point added")
        print("Score =" + " " + str(score))
    if guess2ndprice == "1500":
        print("Incorrect, no point")
        print("Score =" + " " + str(score))

    guess3rdprice = input("How much does a 15-inch model Apple MacBook pro coat $6,000 or $5,000")
    while guess3rdprice not in numbercost:
        print("The number you entered was wrong try again")
        guess3rdprice = input("How much does a 15-inch model Apple MacBook pro coat $6,000 or $5,000")
    if guess3rdprice == "6000":
        print("Correct, 1 point added")
        score += 1
        print("Score =" + " " + str(score))
    if guess3rdprice == "5000":
        print("Incorrect, no point")
        print("Score =" + " " + str(score))

    guess4thprice = input("How much does a lamborghini aventador cost  $400,000 or 500,000")
    while guess4thprice not in numbercost:
        print("The number you entered isn't an option")
        guess4thprice = input("How much does a lamborghini aventador cost  $400,000 or 500,000")
    if guess4thprice == "400000":
        score += 1
        print("Correct, 1 point added")
        print("Score =" + " " + str(score))
    if guess4thprice == "500000":
        print("Incorrect, sorry no point")
        print("Score =" + " " + str(score))

    guess5thprice = input("How much do Jordan 11 Concords cost $220 or $150")
    while guess5thprice not in numbercost:
        print("I number you entered isn't an option")
        guess5thprice = input("How much do Jordan 11 Concords cost $220 or $150")
    if guess5thprice == "220":
        print("Correct, 1 point added")
        score += 1
        print("Score =" + " " + str(score))
    if guess5thprice == "150":
        print("Incorrect, sorry no point")
        print("Score =" + " " + str(score))

    guess6thprice = input("How much do Jordan 12s cost $135 or $150")
    while guess6thprice not in numbercost:
        print("The number you entered isn't an option")
        guess6thprice = input("How much do Jordan 12s cost $135 or $150")
    if guess6thprice == "135":
        print("Correct, 1 point added")
        score += 1
        print("Score =" + " " + str(score))
    if guess6thprice == "150":
        print("Incorrect, sorry no point")
        print("Score =" + " " + str(score))

    guess7thprice = input("how much do Air Pods pro cost $250 or $200")
    while guess7thprice not in numbercost:
        print("The number you entered isn't an option")
        guess7thprice = input("how much do Air Pods pro cost $250 or $200")
    if guess7thprice == "250":
        print("Correct, 1 point added")
        score += 1
        print("Score =" + " " + str(score))
    if guess7thprice == "200":
        print("Incorrect, no point")
        print("Score =" + " " + str(score))
    if str(score) > opposcorebeat:
        print("You Won your opponent. Your random free prize is" + " " + random.choice(randomprize) + " " +
              "Congratulations, Thanks for Playing")
    else:
        print("You lost to your opponent. Sorry you get no free prize, Thanks for playing")


guessprice()
