def beverage():
    price = 0
    question = input("Would you like a beverage?: ").lower()
    if question == "yes".lower():
        size = input("What kind of size would you want?: ").lower()
        if size == "small".lower():
            price += 1.00
            print("Total will be %.2f" % price)
        if size == "Medium".lower():
            price += 1.75
            print("Total will be %.2f" % price)
        if size == "Large".lower():
            price += 2.25
            print("Total will be %.2f" % price)

        if question == "no".lower():
            return False


beverage()