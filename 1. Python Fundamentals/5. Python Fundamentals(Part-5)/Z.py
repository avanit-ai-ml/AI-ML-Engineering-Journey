# Assignment Problem

# 1. Create a program that: 1. Opens a file "name.txt" in write mode 2. Write five names (one per line) entered by the user 3. Then opens the same file in the read mode and prints all names.
'''
with open("NameList.txt", "w") as f:
    for i in range(5):
        if i != 4:
            name = input("Enter name: ")
            f.write(name)
            f.write("\n")
        else:
            name = input("Enter name: ")
            f.write(name)
with open("NameList.txt", "r") as f:
    print(f.read())
'''
# 2. Create a program that: 1. Opens a file "log.txt" in append mode 2. Add a new log entry (like "Program run successfully") 3. Open the file in read mode and print all logs
'''
with open("log.txt", "a") as f:
    f.write("Program run successfully\n")
    f.write("Program run successfully\n")
    f.write("Program run successfully\n")
    f.write("Program run successfully\n")
    f.write("Program run successfully")

with open("log.txt", "r") as f:
    print(f.read())
'''

# 3. Create a program that: 1. Has a list of numbers: [5, 10, 15, 20, 25] 2. Use a list comprehension to create a new list with only numbers greater than 15 3. Print the new list.
'''
num = [5, 10, 15, 20, 25]

new_num = [el for el in num if el > 15]

print(new_num)
'''

# 4. Create a Python dictionary of 3 cities and their populations. Save it to "cities.json". 1. Then use the JSON and print each city and its population. 2. Ask the user for a new city & its population - update this info in the json file.
'''
import json

py_dict = {
    "Delhi": 1200000,
    "Mumbai": 9000000,
    "Patna": 890000
}

with open("cities.json", "w") as f:
    json.dump(py_dict, f, indent=4)
    print("Data Saved Successfully.")

with open("cities.json", "r") as f:
    cities = json.load(f)

    for city, population in cities.items():
        print(f"{city}: {population}")

city = input("Enter city name: ")
pop = int(input(f"{city}'s population: "))

cities[city] = pop

with open("cities.json", "w") as f:
    json.dump(cities, f, indent=4)
    print("New data saved successfully.")
'''

# 5. Write a program that tries to open "datad.txt" in read mode. If the file doesn't exist, catch the exception and print "File not found!".
try:
    with open("datad.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("File not found!")
else:
    print(data)