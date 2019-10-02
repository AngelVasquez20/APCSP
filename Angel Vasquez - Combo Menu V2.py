import sys
total = 0

sandwich_list = ["chicken", "tofu", "beef"]
sizes = ["small", "medium", "large"]
answers = []
yes_cost = []


def sandwich():
    sand_question = input("Would you like a sandwich (Type in yes or no)? ")
    sandqprice = 0
    if sand_question == "no":
        answers.append(0)
        yes_cost.append(int(0))
        return sandqprice
    if sand_question == "q":
        sys.exit(0)
    if sand_question == "yes":
        ask = input("What kind of sandwich would you like chicken, tofu, or beef:").lower()
        if ask in sandwich_list:
            if ask == sandwich_list[0]:
                sandqprice += 5.25
                print("You ordered a Chicken sandwich")
                answers.append(ask)
                yes_cost.append(sandqprice)
            elif ask == sandwich_list[1]:
                sandqprice += 5.75
                print("You ordered a Tofu sandwich")
                answers.append(ask)
                yes_cost.append(sandqprice)
            elif ask == sandwich_list[2]:
                sandqprice += 6.25
                print("You have ordered a Beef sandwich")
                answers.append(ask)
                yes_cost.append(sandqprice)
        return sandqprice
    while sand_question is not "yes" or sand_question is not "no":
        sand_question = input("Invalid information. Would you like a sandwich (yes or no)")


sandwich()


def beverage():
    beverageprice = 0
    question = input("Would you like a beverage?: ").lower()
    if question == "yes".lower():
        size = input("What kind of size would you want?: ").lower()
        if size == "small".lower():
            beverageprice += float(1.00)
            print("You ordered a small beverage")
            return False
        if size == "medium".lower():
            beverageprice += float(1.75)
            print("You ordered a medium beverage")
        if size == "large".lower():
            beverageprice += float(2.25)
            print("You ordered a large beverage")
        if question == "no".lower():
            return False
        return beverageprice


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
        else:
            return packet_cost
        if total > 7.25:
            packet_cost += (0.07 * (total - 1) + packet_cost)
            print("Your total will be $%.2f" % packet_cost)
            return packet_cost

        else:
            packet_cost += (0.07 * (total + packet_cost))
            print("Your total will be $%.2f" % packet_cost)
            return packet_cost

ketchup()


# total += sandwich()
# total += beverage()
# total += french_fries()
# total += ketchup()
