# 5. Match Case

color = input("Enter The Traffic Light Color: ")

match color:
    case "red":
        print("Stop - Until Light Turns Green")
    case "yellow":
        print("Caution - The Light is About to Turn Red")
    case "green":
        print("Go - You may Proceed. Always make sure the intersection is clear...")
    case _: # -------> Default Case
        print("Something went wrong")
