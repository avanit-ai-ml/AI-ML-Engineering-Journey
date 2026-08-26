# 10. Loop using for

'''
str = input("Enter a string: ")

for ch in str:
    print(ch)
'''

'''
str = input("Enter a string: ")

if 'i' in str: # in is called Membership Operator
    print("i present in", str)
'''

'''
for i in range(29):
    print(i)
'''

word = "Artificial intelligence"
count = 0
for ch in word:
    if ch == 'i':
        count += 1
print("Total Number of i in", word,":", count)