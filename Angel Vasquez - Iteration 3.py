def french_fries():
    price = 0
    order = input("Would you like some french fries?")
    if order == "yes":
        size = input("What size would you like?")
        if size == "small":
            price += 1.00
            mega_size = input("Would you like a mega size?")
            if mega_size == "yes":
                price += 2.00
                print("Your mega size will be %.2f" % price)
            else:
                print()

        if size == "Medium":
            price += 1.50
            print("Your total will be $%.2f" % price)

        if size == "Large":
            price += 2.00
            print("Your total will be $%.2f" % price)

    if order == "no":
        return False


french_fries()