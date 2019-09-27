def french_fries():
    order = input("Would you like some french fries?")
    french_fries_price = 0
    if order == "yes":
        size = input("What size would you like?")
        if size == "small".lower():
            french_fries_price += float(1.00)
            mega_size = input("Would you like a mega size?")
            if mega_size == "yes".lower():
                french_fries_price += float(2.00)
                print("You  ordered mega fries")
                return False
            if mega_size == "no".lower():
                print("You ordered small fries")
                return False
        if size == "medium".lower():
            french_fries_price += float(1.50)
            print("You ordered medium fries")
            return False
        if size == "large".lower():
            french_fries_price += float(2.00)
            print("You ordered large fries")
            return False
        if order == "no":
            return False
        return french_fries_price
    else:
        print("I didn't get that")
        return french_fries()


french_fries()