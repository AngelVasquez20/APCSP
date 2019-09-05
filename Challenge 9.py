def atom():
    carbon = int(input("Enter the number of carbon atoms?"))
    hydrogen = (carbon * 2) + 2
    atomic_weight = (carbon * 12) + hydrogen
    print("The atomic mass of " + "C" + str(carbon) + "H" + str(hydrogen) + " is " + str(atomic_weight))


atom()
