# 4. Nesting

num = int(input("Enter a Number: "))

if num%2 == 0:
    if num > 0:
        print(num, "is Even & Positive")
    elif num == 0:
        print(num, "is Even & Zero")
    else:
        print(num, "is Even & Negative")
else:
    if num < 0:
        print(num, "is Negative & Odd")
    else:
        print(num, "is Positive & Odd")