# 19. Factorial of N

num = int(input("Enter a Number: "))

def factorial(num):
    fact = 1
    for i in range(num):
        fact *= i+1
    return fact
print("Factorial of", num,"is: ",factorial(num))