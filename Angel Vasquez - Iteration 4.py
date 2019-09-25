def amount(a):
    return float(a) * .25


def ketchup():
    price = 0
    ketchup_q = input("Would you like some ketchup?")
    if ketchup_q == "yes":
        count = int(input("How many packets would you like? "))
        price = price + amount(count)
    else:
        print("The total cost is" + "" + str(price))


ketchup()