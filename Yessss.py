def user():
    user = input("Enter a number: ")
try: #Try to see if this works
    print(int(user))
except ValueError: # if error, don't crash. Do this instead.
    print("That's not an integer. ")
    return user
else: #if no error occurs, do this
    print("That was an integer. All good here.")
    print("This line always happens.")