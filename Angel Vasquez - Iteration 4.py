total = 0

def ketchup():
    packet_cost = 0
    ketchup_q = input("Would you like some ketchup")
    if ketchup_q == "yes":
        ask = int(input("How many packets would you like"))
        if ask >= 1:
            packet_cost += float(ask * 0.25)
            print("Your total coast is %.2f" % packet_cost)
        else:
            return packet_cost
        if total > 7.25:
            packet_cost += (0.07 * (total - 1) + packet_cost)
            return packet_cost

        else:
            packet_cost += (0.07 * (total + packet_cost))
            return packet_cost


ketchup()