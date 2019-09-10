number = int(input("fe"))
if number <= -273 and number <= 12:
    print("Solid")
elif number > 13 and number < 47:
    print("Liquid")
elif number >= 47:
    print("Gas")
else:
    print("Not found")