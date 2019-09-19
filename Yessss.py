import math
usersOption = str(input("Please enter a mathematical function of your choice"))
numberOne = float(input("Please enter the first number"))
numberTwo = float(input("Please enter the second number"))
if usersOption == "integer":
    answer = int(numberOne + numberTwo)
elif usersOption == "modulus":
    answer = numberOne%numberTwo
    answer = numberOne%answer
elif usersOption == "ceiling":
    answer = math.ceil(numberOne + numberTwo)
    answer = math.ceil(answer/2)
elif usersOption == "square":
    answer = pow((int(numberOne) + int(numberTwo)),2)
    answer = pow(int(numberOne),2) + answer
elif usersOption == "round":
    answer = round((numberOne + numberTwo),1)
    answer = round(answer + 0.7,0)
else:
    answer = int(numberOne)+pow(numberTwo,2)+math.ceil(numberOne)+round(numberTwo,2)
print(answer)