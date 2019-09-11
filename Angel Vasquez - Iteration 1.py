def sandwich():
    price = 0
    sandq = input("What kind of sandwich would you like to buy? Enter 1 for chicken, Enter 2 for beef, "
                  "Enter 3 for tofu: ")
    if sandq == "1":
        price += float(5.25)
        print("You ordered a chicken sandwich, that will be $%.2f" % price)

    if sandq == "2":
        price += float(6.25)
        print("You ordered a beef sandwich, that will be $%.2f" % price)

    if sandq == "3":
        price += float(5.75)
        print("You ordered a tofu sandwich, that will be $%.2f" % price)


sandwich()
