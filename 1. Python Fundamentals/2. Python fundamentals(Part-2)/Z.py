# Assignment Problem

# 1. Write a program that takes salary as input. Using conditional statements, calculate the tax amount based on these rules: If the salary is less than 30,000, the tax rate is 5%. If the salary is 30,000 to 70,000, the tax rate is 15%. If the salary is greater than 70,000, the tax rate is 25%.
'''
salary = float(input("Enter Salary: "))

def tax_calculator(salary, rate):
    return (salary*rate*0.01)

if salary < 30000:
    print("Tax: ", tax_calculator(salary, 5))
elif (salary >= 30000 and salary < 700000):
    print("Tax: ", tax_calculator(salary, 15))
else:
    print("Tax: ", tax_calculator(salary, 25))
'''

# 2. Write a function that takes two integers a & b as input and prints all the even numbers between them, (inclusive).
'''
num_1 = int(input("Enter First Number: "))
num_2 = int(input("Enter Second Number: "))

for num in range(num_1, num_2+1, 1):
    if num%2 == 0:
        print(num)
'''

# 3. Write a function that prints the digits of a number. Example: For the number 312, there are 3 digits: 3, 1, and 2. The function should print each digit separately.
'''
num = input("Enter a Number: ")

def digit_printer(num):
    for ch in num:
        print(ch)
digit_printer(num)
'''

# 4. Write a function that returns the number of digits in a given number.
'''
num = input("Enter a number: ")

def count_digit(num):
    count = 0
    for i in num:
        count +=1
    return count

print("Total Digit in", num, ":", count_digit(num))
'''

# 5. Write a function that returns the sum of digits of a given number.
'''
num = input("Enter a number: ")

def sum_of_digits(num):
    sum = 0
    for i in num:
        sum += int(i)
    print(sum)
sum_of_digits(num)
'''

# 6. Write a program to print all numbers from 1 to 100 that are divisible by both 3 and 5.
'''
num = input("Enter a number: ")

def multiple(num):
    for i in range(1, int(num)):
        if i%3 == 0 and i %5 ==0:
            print(i)
multiple(num)
'''

# 7. Design a program that continuously takes a number as input from the user and prints whether the number is positive or negative. The program should continue running until the user enters "Quit".
'''
while True:
    num = input("Enter a Number: ")

    if num == "Quit":
        break
    else:
        if int(num)%2 == 0:
            print(num, "--> EVEN")
        else:
            print(num, "--> ODD")
'''

# 8. Write a function named calculator(a, b, operation) that takes three parameters: a – the first number b – the second number operation – the arithmetic operation to perform The function should perform addition, subtraction, multiplication, or division based on the value of the operation parameter.
'''
num1 = float(input("Enter first Number: "))
num2 = float(input("Enter second Number: "))
op = input("Enter operation(+, -, *, /): ")

def calc(num1, num2, op):
    match op:
        case '+':
            print((num1+num2))
        case '-':
            print((num1-num2))
        case '*':
            print((num1*num2))
        case '/':
            print((num1/num2))
        case _:
            print("Something Went Wrong...")
calc(num1,num2,op)
'''

# 9. Write a function is_prime(n) that returns True if n is prime and False otherwise, using a loop.
'''
num = int(input("Enter a Number: "))

def is_prime(num):
    for i in range(2, num):
        if num%i == 0:
            print("False")
            return
    print("True")
is_prime(num)
'''

# 10. Create a Number Guessing Game. Choose a secret number in advance and write a program that asks the user to guess it. The program should print: "Too high" if the guess is greater than the secret number. "Too low" if the guess is less than the secret number. "Correct" if the guess matches the secret number.
secret_number = 18

while True:
    num = int(input("Enter a Number: "))
    if num > secret_number:
        print("Too High")
    elif num < secret_number:
        print("Too Low")
    else:
        print("Correct Match")
        break