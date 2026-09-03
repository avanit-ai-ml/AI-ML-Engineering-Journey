# 7. Exception Handling

try:
    a = int(input("Enter first number: "))

    b = int(input("Enter second number: "))

    ans = a/b

except ZeroDivisionError:
    print("Second number can't ne zero")

except ValueError:
    print("Enter integers only.")

else:
    print(ans)
