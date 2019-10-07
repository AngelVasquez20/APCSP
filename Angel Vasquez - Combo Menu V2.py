import sys
total = 0

sandwich_list = ["chicken", "tofu", "beef"]
sizes = ["small", "medium", "large"]
answers = []
yes_cost = []
orders = []


def sandwich():
    sandqprice = 0
    sand_question = input("Would you like a sandwich (Type in yes or no)? ")
    if sand_question == "quit" or sand_question == "q":
        sys.exit()
    if sand_question == "no":
        yes_cost.append(int(0))
        return
    if sand_question == "yes":
        ask = input("What kind of sandwich would you like chicken, tofu, or beef:").lower()
        while ask not in sandwich_list:
            if ask == "quit" or ask == "q":
                print("Thanks, bye")
                sys.exit()
            print("I din't get that. You can enter q or quit ro end this code")
            ask = input("What kind of sandwich would you like chicken, tofu, or beef:").lower()
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


def beverage():
    beverageprice = 0
    question = input("Would you like a beverage?(yes or no): ").lower()
    if question == "no":
        sys.exit()
    if question == "yes".lower():
        size_q = input("What kind of size would you want?(small, medium, or large): ").lower()
        if size_q in sizes:
            if size_q == sizes[0]:
                beverageprice += 1.00
                print("You have ordered a small beverage")
                answers.append(size_q)
                yes_cost.append(size_q)
            elif size_q == sizes[1]:
                beverageprice += 1.75
                print("You ordered a medium beverage")
                answers.append(size_q)
                yes_cost.append(size_q)
            elif size_q == sizes[2]:
                beverageprice += 2.25
                print("You have ordered a large beverage")
                answers.append(size_q)
                yes_cost.append(size_q)
        return beverageprice


def french_fries():
    order = input("Would you like some french fries? (yes or no)")
    while order is not "yes" or order is not "no":
        print("I didn't get that")
        order = input("would you like some french fries(yes, no)")
        french_fries_price = 0
        if order == "yes":
            french_size = input("What size would you like?(small, medium, or large)")
            if french_size in sizes:
                if french_size == sizes[0]:
                    french_fries_price += 1.00
                    mega_size = input("Would you like a mega size(yes or no)")
                    if mega_size == "yes":
                        french_fries_price += 2.00
                        print("You have ordered mega fries")
                    if mega_size == "no":
                        print("You ordered small fries")
                    answers.append(french_size)
                    yes_cost.append(french_size)
                elif french_size == sizes[1]:
                    french_fries_price += 1.50
                    print("You have ordered medium french fries")
                    answers.append(french_size)
                    yes_cost.append(french_size)
                elif french_size == sizes[2]:
                    french_fries_price += 2.00
                    print("You have ordered large french fries")
                    answers.append(french_size)
                    yes_cost.append(french_size)
            return french_fries_price


def ketchup():
    packet_cost = 0
    ketchup_q = input("Would you like some ketchup(yes or no)")
    if ketchup_q == "q":
        sys.exit(0)
    if ketchup_q == "yes":
        ask = int(input("How many packets would you like"))
        if ask >= 1:
            packet_cost += float(ask * 0.25)
        randomtot = ((yes_cost[0] + yes_cost[1] + yes_cost[2]) + packet_cost)
        print(randomtot)
        if len(answers) == 3:
            print("Your total is $%.2f plus tax" % (randomtot + (0.07 * randomtot) - 1))
        else:
            print("Your total is $%.2f plus tax" % (randomtot + (0.07 * randomtot)))
        return packet_cost


def receipt():
    for i in orders:
        print(i)
        print("total was $%.2f" % total)


def again():
    order_again = input("Would you like to order")
    yes = 0
    while order_again == "yes" or order_again == "no":
        if order_again == "no":
            print(orders)
            print("Your total for everything  is $%.2f" % yes)
            sys.exit(0)
        yes += sandwich()
        yes += beverage()
        yes += french_fries()
        yes += ketchup()
        print(yes)
        orders.append(answers)
        print(orders)
        for i in answers:
            answers.remove(i)
        order_again = input("Would you like to order again")


again()
