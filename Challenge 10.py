def standard():
    par_3 = int(input("How many par 3 holes are there?"))
    par_5 = int(input("How many par 5 holes are there?"))

    adjust = int(input("Difficulty adjustment?"))

    shot_3 = (par_3 * 3)
    shot_5 = (par_5 * 5)

    scratch = (shot_5 + shot_3) - adjust
    print("The standard scratch is " + str(scratch))


standard()
