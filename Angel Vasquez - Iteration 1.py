def sandwich():
    price = 0
    sandq = input("What kind of sandwich would you like to buy: ")
    if sandq == "chicken":
        price += 5.25
        print()

    if sandq == "beef":
        price += 6.25

    if sandq == "tofu":
        price += 5.75


sandwich()
