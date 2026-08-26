# 9. Break & Continue

while True:
    num = int(input("Enter a Number: "))

    if num%2 == 0:
        print(num, "is Even.")
        continue
    else:
        print(num, "is Even.")
        break