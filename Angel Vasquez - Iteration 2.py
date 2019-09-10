def beverage():
    question = input("Would you like a beverage: ")
    if question == "yes":
        input("What kind of size would you want: ")

    if question == "no":
        return False


beverage()