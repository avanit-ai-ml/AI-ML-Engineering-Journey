# 16. Practice Examples (Function)
'''
num1 = float(input("Enter Fisrt Number: "))
num2 = float(input("Enter Second Number: "))
num3 = float(input("Enter Third Number: "))

def avg_of_three_nums(num1, num2, num3):
    sum = (num1+num2+num3)
    return sum/3
print("Average of", num1, num2, num3,": ", avg_of_three_nums(num1, num2, num3))
'''


'''
num1 = float(input("Enter Fisrt Number: "))
num2 = float(input("Enter Second Number: "))

def avg_of_three_nums(num1, num2, num3 = 10):
    sum = (num1+num2+num3)
    return sum/3
print("Average of", num1, num2,": ", avg_of_three_nums(num1, num2))
'''