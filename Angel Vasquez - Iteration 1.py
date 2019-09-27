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