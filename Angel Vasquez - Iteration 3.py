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
