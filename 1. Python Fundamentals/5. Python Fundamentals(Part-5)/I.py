# 9. List Comprehension

list = [i**2 for i in range(1, 101) if i%2 == 0]

print(type(list))

print(list)


num = [-9, 7, -2, 5, 8, 6]

num2 = [0 if val < 0 else val for val in num]

print(num2)