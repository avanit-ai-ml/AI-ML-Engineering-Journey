# 12. Set Methods

s = {1, 2, 2, 3, 5, 4, 4}

print(s)

s.add(8)
print(s)

s.remove(8)
print(s)

s.pop()
print(s)

s1 = {9, 12, 24, 4}
s2 = s.union(s1)
print(s2)

s2 = s.intersection(s1)
print(s2)