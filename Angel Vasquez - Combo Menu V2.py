import sys
total = 0

sandwich_list = ["chicken", "tofu", "beef"]
sizes = ["small", "medium", "large"]
answers = []
yes_cost = []
orders = []


def sandwich():
    sand_question = input("Would you like a sandwich (Type in yes or no)? ")
    sandqprice = 0
    if sand_question == "no":
        yes_cost.append(int(0))
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
        print("I didn't get that")
        sand_question = input("Would you like a sandwich (Type in yes or no)? ")


def beverage():
    beverageprice = 0
    question = input("Would you like a beverage?(yes or no): ").lower()
    if question == "no":
        sys.exit(0)
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
    # while order is not "yes" or order is not "no":
    #     print("I didn't get that")
    #     order = input("would you like some french fries(yes, no)")


def ketchup():
    packet_cost = 0
    ketchup_q = input("Would you like some ketchup(yes or no)")
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


def receipt():
    for i in orders:
        print(i)
        print("total was $%.2f" % total)


def again():
    order_again = input("Would you like to order")
    while order_again == "yes" or order_again == "no":
        if order_again == "no":
            # receipt()
            # sys.exit(0)
            return
        sandwich()
        beverage()
        french_fries()
        ketchup()
        print(total)
        orders.append(answers)
        print(orders)
        for i in answers:
            answers.remove(i)
        order_again = input("Would you like to order again")


again()
