# 14. Sum of N natural Numbers
num = int(input("Enter a number: "))
sum = 0
for i in range(num):
    sum += i+1
print("Sum: ", sum)