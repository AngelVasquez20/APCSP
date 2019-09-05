def telephone():
    area_code = input("What is your area code?")
    prefix = input("What is the prefix of your number (first three numbers)?")
    suffix = input("What is the suffix of your number (last four numbers)?")

    print("You have entered: ")
    print("1" + "(" + area_code + ")" + prefix + "-" + suffix)


telephone()
