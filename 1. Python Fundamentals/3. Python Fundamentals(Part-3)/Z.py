# Assignment Problem
# 1. Ask the user for a string and check whether it is a palindrome or not. A palindrome is a string that is the same when read forward and backward. Examples: “madam”, “racecar”, etc.
'''
str = input("Enter a string: ")

def palindrome_checker(str):
    for i in range(len(str)):
        if i >= len(str)-i-1 and str[i] != str[len(str)-i-1]:
            print("Not a Palindrom")
            return
    print("Palindrome")
palindrome_checker(str)
'''

# 2. Given a list of integers, compute the average of all the numbers in the list.
'''
integ = [1, 3, 9, 9, 7, 8, 2]

def avg_of_all_number(integ):
    sum = 0
    for val in integ:
        sum += val
    return sum/len(integ)
print(f"{avg_of_all_number(integ):.2f}")
'''

# 3. Input two lists of integers from the user. Merge them into one list and sort the resulting list. Example: list1 = [1, 2, 7] list2 = [2, 4, 5] result = [1, 2, 2, 4, 5, 7]
'''
list1 = []
list2 = []
while True:
    num = input("List1 Enter a Digits(or Quit): ")
    if num != "Quit":
        list1.append(int(num))
    else:
        break
while True:
    num = input("List2 Enter a Digits(or Quit): ")
    if num != "Quit":
        list2.append(int(num))
    else:
        break

uni = set(list1).union(set(list2))

result = list(uni)

print(result)
'''

# 4. Given a tuple of integers, create: A tuple of all even numbers. A tuple of all odd numbers.
'''
list1 = []
list_odd = []
list_even = []

while True:
    num = input("Enter Tupple Element(or Quit): ")
    if num != "Quit":
        list1.append(int(num))
    else:
        break

for val in list1:
    if val%2 == 0:
        list_even.append(val)
    else:
        list_odd.append(val)
print(tuple(list_even))
print(tuple(list_odd))
'''

# 5. Create a dictionary where: Keys = student names Values = marks (integers) Write a menu-based program where the user presses a key (A, B, C, or D) depending on the operation they want to perform: Add a student — A Update marks — B Search for a student — C Display all students and marks — D
'''
info_dict = {}

while True:
    op = input("--------- Choose Options --------- \n\nA - Add a Student\nB - Update Marks\nC - Search for a Student\nD - Display all Students and Marks\nQ - Quit Program\n\n")
    match op:
        case 'A':
            s_name = input("Enter Student Name: ")
            s_mark = input("Enter Student Marks: ")
            info_dict.update({
                s_name : s_mark
            })
            print("Student Info Added Successfully")
        case 'B':
            s_name = input("Enter Student Name: ")
            s_mark = input("Enter Student Updated Marks: ")
            if info_dict.keys() == None:
                print("Student doesn't Exist")
            else:
                info_dict.update({
                    s_name : s_mark
                })
                print("Student info Updated Successfully")
        case 'C':
            s_name = input("Enter Student Name: ")
            if info_dict.keys() == None:
                print("Student doesn't Exist")
            else:
                print(info_dict.get(s_name))
        case 'D':
            print(info_dict)
        case 'Q':
            print("Program Terminated Successfully")
            break
'''

# 6. Given a list of words: word = ["apple", "banana", "kiwi", "cherry", "mango"] Create a dictionary that map each word to its length.
'''
words = ["apple", "banana", "kiwi", "cherry", "mango"]
dict_info = {}
for word in words:
    dict_info.update({
        word : len(word)
    })
print(dict_info)
'''

# 7. Write a program that takes a string from the user and prints the number of spaces in the string.
'''
str = input("Enter a string: ")
count = 0
for ch in str:
    if ch == " ":
        count += 1
print(f"Total spaces: {count}")
'''

# 8. Write a program to check whether two lists share no common elements
'''
# list_one = [1, 2, 3, 4]
# list_two = [5, 6, 7, 8]

list_one = [1, 2, 3]
list_two = [3, 4]

if len(set(list_one).intersection(set(list_two))) == 0:
    print("Share no common elements")
else:
    print("Share common elements")
'''

# 9. Given a list, print all elements that appear more than once in the list.
'''
list_one = [1, 2, 3, 4, 2, 4]

for val in list(set(list_one)):
    list_one.remove(val)
print(list_one)
'''

# 10. Ask the user for a string and print: All unique characters, The count of unique characters
'''
str = input("Enter a string: ")

ch_set = set()
for ch in str:
    ch_set.add(ch)
print(ch_set)

str_list = list(str)
uniq_char_count = 0

for ch in ch_set:
    if str_list.count(ch) == 1:
        uniq_char_count += 1
print(f"Total Unique Character(s): {uniq_char_count}")
'''