def sandwich():
    price = 0
    sandq = input("What kind of sandwich would you like to buy? Enter 1 for chicken, Enter 2 for beef, "
                  "Enter 3 for tofu: ")
    if sandq == "1":
        price += float(5.25)
        print("You ordered a chicken sandwich, that will be $%.2f" % price)

    if sandq == "2":
        price += float(6.25)
        print("You ordered a beef sandwich, that will be $%.2f" % price)

    if sandq == "3":
        price += float(5.75)
        print("You ordered a tofu sandwich, that will be $%.2f" % price)
    return price


sandwich()


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


def french_fries():
    price = 0
    order = input("Would you like some french fries?")
    if order == "yes":
        size = input("What size would you like?")
        if size == "small".lower():
            price += 1.00
            mega_size = input("Would you like a mega size?")
            if mega_size == "yes".lower():
                price += 2.00
                print("Your mega size will be $%.2f" % price)
            if mega_size == "no".lower():
                print("Your small beverage will be $%.2f" % price)
                return False
        if size == "Medium":
            price += 1.50
            print("Your total will be $%.2f" % price)

        if size == "Large":
            price += 2.00
            print("Your total will be $%.2f" % price)
    if order == "no":
        return False
    if order is None:
        raise KeyError
    print("I didn't get that")
    return french_fries()


french_fries()

