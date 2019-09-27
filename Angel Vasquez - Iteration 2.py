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
