import sys
total = 0

sandwich_list = ["chicken", "tofu", "beef"]
sizes = ["small", "medium", "large"]
yes_no_answers = ["yes", "no"]
answers = []
yes_cost = []
orders = []


def sandwich():
    sandqprice = 0
    sand_question = input("Would you like a sandwich (Type in yes or no)? ").lower()
    while sand_question not in yes_no_answers:
        if sand_question == "quit" or sand_question == "q":
            print("Thanks, bye")
            sys.exit()
        print("I didn't get that. If you don't want to order you can enter quit or q")
        sand_question = input("Would you like a sandwich (Type in yes or no)?").lower()
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
    while question not in yes_no_answers:
        if question == "quit" or question == "q":
            print("Thanks, bye")
            sys.exit()
        print("I didn;t get that. If you don't want to order enter quit or q")
        question = input("Would you like a beverage?(yes or no): ")
    if question == "no":
        sys.exit()
    if question == "yes".lower():
        size_q = input("What kind of size would you want?(small, medium, or large): ").lower()
        while size_q not in sizes:
            if size_q == "quit" or size_q == "q":
                print("Thanks, bye")
                sys.exit()
            print("I didn't get that. If you don't want to order enter quit or q")
            size_q = input("What kind of size would you want?(small, medium, or large): ").lower()
        if size_q == sizes[0]:
            beverageprice += 1.00
            print("You have ordered a small beverage")
            answers.append(size_q)
            yes_cost.append(beverageprice)
        elif size_q == sizes[1]:
            beverageprice += 1.75
            print("You ordered a medium beverage")
            answers.append(size_q)
            yes_cost.append(beverageprice)
        elif size_q == sizes[2]:
            beverageprice += 2.25
            print("You have ordered a large beverage")
            answers.append(size_q)
            yes_cost.append(beverageprice)
    return beverageprice


def french_fries():
    french_fries_price = 0
    order = input("Would you like some french fries? (yes or no)").lower()
    while order not in yes_no_answers:
        if order == "quit" or order == "q":
            print("Thanks, bye")
            sys.exit()
        print("I didn't get that. If you don't want to order enter quit or q")
        order = input("Would you like some french fries? (yes or no)").lower()
    if order == "yes":
        french_size = input("What size would you like?(small, medium, or large)").lower()
        while french_size not in sizes:
            if french_size == "quit" or french_size == "q":
                print("Thanks, bye")
                sys.exit()
            print("I didn't get that. If you don't want to order enter quit or q")
            french_size = input("What size would you like?(small, medium, or large)").lower()
        if french_size == sizes[0]:
            french_fries_price += 1.00
            mega_size = input("Would you like a mega size(yes or no)")
            if mega_size == "yes":
                french_fries_price += 2.00
                print("You have ordered mega fries")
                answers.append(french_size)
                yes_cost.append(french_fries_price)
            if mega_size == "no":
                print("You ordered small fries")
                answers.append(french_size)
                yes_cost.append(french_fries_price)
        elif french_size == sizes[1]:
            french_fries_price += 1.50
            print("You have ordered medium french fries")
            answers.append(french_size)
            yes_cost.append(french_fries_price)
        elif french_size == sizes[2]:
            french_fries_price += 2.00
            print("You have ordered large french fries")
            answers.append(french_size)
            yes_cost.append(french_fries_price)
    return french_fries_price


def ketchup():
    packet_cost = 0
    ketchup_q = input("Would you like some ketchup(yes or no)")
    while ketchup_q not in yes_no_answers:
        if ketchup_q == "quit" or ketchup_q == "q":
            print("Thanks, bye")
            sys.exit()
        print("I didn't get that if you don't want to order enter q or quit")
        ketchup_q = input("Would you like some ketchup(yes or no)")
    if ketchup_q == "no":
        return
    if ketchup_q == "yes":
        ask = int(input("How many packets would you like"))
        if ask >= 1:
            packet_cost += float(ask * 0.25)
        random_total = ((yes_cost[0] + yes_cost[1] + yes_cost[2]) + packet_cost)
        if len(answers) == 3:
            print("Your total is $%.2f plus tax" % (random_total + (0.07 * random_total) - 1))
        else:
            print("Your total is $%.2f plus tax" % (random_total + (0.07 * random_total)))
        return packet_cost


def receipt():
    for i in orders:
        print(i)
        print("total was $%.2f" % total)


def again():
    order_again = input("Would you like to order")
    while order_again == "yes" or order_again == "no":
        if order_again == "no":
            print(orders)
            sys.exit()
        sandwich()
        beverage()
        french_fries()
        ketchup()
        orders.append(answers)
        print(orders)
        for i in answers:
            answers.remove(i)
        order_again = input("Would you like to order again")


again()
