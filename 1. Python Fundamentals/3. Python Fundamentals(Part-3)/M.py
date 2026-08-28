# 13. Practice Problem(Part a & b)
# Give a list of tuples with info (name, subject)
info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English"),
]

# a. List all unique course
unique_couse = set()

for val in range(len(info)):
    unique_couse.add(info[val][1])
print(unique_couse)

# b. List student enrolled in english
for val in range(len(info)):
    if info[val][1] == "English":
        print(info[val][0])