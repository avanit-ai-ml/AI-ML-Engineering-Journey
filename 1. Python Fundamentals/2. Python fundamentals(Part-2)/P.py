# 18. Lambda Function

num1 = int(input("Enter first Number: "))
num2 = int(input("Enter second Number: "))

sum = lambda num1,num2: num1+num2

print("Sum: ", sum(num1, num2))