price = 0

def sandwich():
    sandq = input("What kind of sandwich would you like to buy? Enter 1 for chicken, Enter 2 for beef, "
                  "Enter 3 for tofu: ")
    sandqprice = 0
    if sandq == "1":
        sandqprice += float(5.25)
        print("You ordered a chicken sandwich, that will be $%.2f" % sandqprice)
        return False
    if sandq == "2":
        sandqprice += float(6.25)
        print("You ordered a beef sandwich, that will be $%.2f" % sandqprice)
        return False
    if sandq == "3":
        sandqprice += float(5.75)
        print("You ordered a tofu sandwich, that will be $%.2f" % sandqprice)
        return False
    if sandq is None:
        raise KeyError
    print("I didn't get that")
    return sandqprice



sandwich()


def beverage():
    beverageprice = 0
    question = input("Would you like a beverage?: ").lower()
    if question == "yes".lower():
        size = input("What kind of size would you want?: ").lower()
        if size == "small".lower():
            beverageprice += 1.00
            print("Total will be %.2f" % beverageprice)
            return False
        if size == "medium".lower():
            beverageprice += 1.75
            print("Total will be %.2f" % beverageprice)
            return False
        if size == "large".lower():
            beverageprice += 2.25
            print("Total will be %.2f" % beverageprice)
            return False
        if question == "no".lower():
            return False
        if question is None:
            raise KeyError
        print("I didn't get that")
        return beverageprice


beverage()


def french_fries():
    
    french_fries_price = 0
    order = input("Would you like some french fries?")
    if order == "yes":
        size = input("What size would you like?")
        if size == "small".lower():
            french_fries_price += 1.00
            mega_size = input("Would you like a mega size?")
            if mega_size == "yes".lower():
                french_fries_price += 2.00
                print("Your mega size will be $%.2f" % french_fries_price)
                return False
            if mega_size == "no".lower():
                print("Your small beverage will be $%.2f" % french_fries_price)
                return False
        if size == "medium".lower():
            french_fries_price += 1.50
            print("Your total will be $%.2f" % french_fries_price)
            return False
        if size == "large".lower():
            french_fries_price += 2.00
            print("Your total will be $%.2f" % french_fries_price)
            return False
    if order == "no":
        return False
    if order is None:
        raise KeyError
    print("I didn't get that")
    return french_fries_price


french_fries()
