def formatting():
    street = input("What is your street address?")
    city = input("What city do you live in?")
    state = input("What is your state abbreviation?")
    zip_code = input("What is your zip code?")

    print(street)
    print(city + "," + state + " " + zip_code)


formatting()
