# 4. Lists in Python

marks1 = 90
marks2 = 94
marks3 = 93
marks4 = 97
marks5 = 98
marks6 = 95

marks = [90, 94, 93, 97, 98, 95]

print(marks[3])
print(type(marks))
print(len(marks))
print(marks[-3])
print(marks)

marks[2] = 99

print(marks)

marks = [90, 94, 93, 97, 98, 95, "Python", 90.18]

print(marks)

# Slicing same as string slicing
print(marks[2:4])