# 1. Conditional Statements in Python
'''
age = 16

if age>=18:
    print("You can Vote")
'''

'''
num = 0

if num > 0:
    print("Positive")
elif num == 0:
    print("Number id Zero")
'''

'''
num = -18

if num > 0:
    print("Positive")
elif num == 0:
    print("Number id Zero")
else:
    print("Negative")
'''

# Traffic Light Example
color = input("Enter The Traffic Light Color: ")

if color == "red":
    print("Stop - Until Light Turns Green")
elif color == "yellow":
    print("Caution - The Light is About to Turn Red")
elif color == "green":
    print("Go - You may Proceed. Always make sure the intersection is clear...")
else:
    print("Something went wrong")