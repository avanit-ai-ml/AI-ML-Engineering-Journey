# 12. Vowel Count

str = input("Enter String: ")
count = 0
for ch in str:
    if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
        count += 1
print("Total Vowel(s): ", count)