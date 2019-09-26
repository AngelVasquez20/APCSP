total = 0


def sandwich():
    sandq = input("Would you like a sandwich: ")
    sandqprice = 0
    if sandq == "yes".lower():
        ask = input("What kind of sandwich would you like 1 for chicken 2 for tofu 3 for beef:")
        if ask == "1":
            print("You ordered a Chicken sandwich")
            sandqprice += float(5.25)
        if ask == "2":
            sandqprice += float(5.75)
            print("You ordered a Tofu sandwich")
        if ask == "3":
            sandqprice += float(6.25)
            print("You ordered a Beef sandwich")
        return sandqprice
    if sandq == "no".lower():
        return False
    else:
        print("I didn't get that")
        return sandwich()


sandwich()


def beverage():
    beverageprice = 0
    question = input("Would you like a beverage?: ").lower()
    if question == "yes".lower():
        size = input("What kind of size would you want?: ").lower()
        if size == "small".lower():
            beverageprice += float(1.00)
            print("You ordered a small beverage")
            # print("Your total so far will be %.2f" % beverageprice)
            return False
        if size == "medium".lower():
            beverageprice += float(1.75)
            print("You ordered a medium beverage")
            return False
        if size == "large".lower():
            beverageprice += float(2.25)
            print("You ordered a large beverage")
            return False
        if question == "no".lower():
            return False
        return beverageprice
    else:
        print("I didn't get that")
        return beverage()


beverage()


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


def ketchup():
    packet_cost = 0
    ketchup_q = input("Would you like some ketchup")
    if ketchup_q == "yes":
        ask = int(input("How many packets would you like"))
        if ask >= 1:
            packet_cost += float(ask * 0.25)
            print("Your total coast is %.2f" % packet_cost)
        else:
            return
        if total > 7.25:
            print("Your total is %.2f plus tax" % (total + (0.07 * (total - 1) + packet_cost)))
            return

        else:
            print("Your total is %.2f plus tax" % (total + (0.07 * packet_cost)))
            return


ketchup()


total += sandwich()
total += beverage()
total += french_fries()
total += ketchup()
print(total)
