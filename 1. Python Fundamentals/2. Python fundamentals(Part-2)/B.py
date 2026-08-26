# 2. Practice Examples(Conditionals)
'''
age = int(input("Enter Your Age: "))

if age < 13:
    print("Child")
elif age >= 13 and age < 18:
    print("Teenager")
else:
    print("Adult")
'''

'''
username = input("Enter Username: ")
password = input("Enter Password: ")

if (username != "admin"):
    print("Wrong Username")
elif (password != "pass"):
    print("Wrong Password")
else:
    print("Successfully loggedin...")
'''


num = int(input("Enter a Number: "))

if num%5 == 0:
    print(num, "is multiple of 5")
else:
    print(num, "is not multiple of 5")