# Assignment Problem

# 1. Write a program that asks the user for their name and age, then prints a sentence like: Hello Shradha, you are 21 years old!
'''
name = input("Enter name: ")
age = int(input("Enter name: "))

print("Hello",name, ", you are",age, "years old!")
'''

# 2. Take two numbers as input from the user and print their: Sum, difference, product, and quotient.
'''
first_num = float(input("First Number: "))
second_num = float(input("Second Number: "))

print("Sum: ",first_num+second_num, "\nDifference: ", first_num-second_num, "\nProduct: ",first_num*second_num, "\nQuotient: ",first_num%second_num)
'''

# 3. Ask the user to enter two integers and one float. Convert them all to floats and print their average.
'''
first_num = int(input("First Integer: "))
second_num = int(input("Second Integer: "))
third_num = float(input("Third Integer: "))

print((float(first_num)+float(second_num)+third_num)/3)
'''

# 4. The user enters a string containing a number (e.g., "45"). Convert it to: an integer a float a string again Print all three values with their types.
'''
str = input("Enter a String: ")

intstr = int(str)

floatstr = float(str)

print(intstr, type(intstr))
print(floatstr, type(floatstr))
print(str, type(str))
'''

# 5. Evaluate and print the result of the following expression: x = 10 + 3 * 2 ** 2, Based on what you learnt in the lecture, explain why the output is what it is.
'''
x = 10 + 3 * 2 ** 2

print(x)
'''

# 6. Write a program to swap values of two numbers entered by the user.
'''
first_num = int(input("First Number: "))
second_num = int(input("Second Number: "))

temp = first_num
first_num = second_num
second_num = temp

print("First Number: ",first_num, "\nSecond Number: ", second_num)
'''

# 7. Ask the user for a temperature in Celsius (string input). Convert it to a float, then calculate and print temperature in Fahrenheit. Conversion formula: FahrenheitTemp = (CelsiusTemp * (9/5)) + 32
'''
temp = input("Enter temp(in celcius): ")

cel_temp = float(temp)

fahrenheit = (cel_temp*(9/5))+32

print(fahrenheit)
'''

# 8. Take the radius as user input and print the area. Use the formula: π × r² (Value of π = 3.14)
'''
radius = float(input("Enter radius: "))

area = 3.14 * radius**2

print("Area: ", area)
'''

# 9. Ask the user for: Principal (P), Rate (R) & Time (T). Convert all to floats and compute simple interest: SI = (P × R × T) / 100
'''
P = float(input("Enter Principal: "))
R = float(input("Enter Rate: "))
T = float(input("Enter Time: "))

SI = (P*R*T)/100

print("Simple Interest:",SI)
'''

# 10. Take a decimal number as input (like 45.78) and output its: Integer part — 45 Fractional part — .78

num = float(input("Enter a floar: "))

print("Integer Part:",int(num),"\nFloating Part:", f"{(num-int(num)):.2f}")
