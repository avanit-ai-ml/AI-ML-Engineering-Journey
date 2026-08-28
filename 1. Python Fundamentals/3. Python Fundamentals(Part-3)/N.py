# 14. Practice Problem(Part c)
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

# c. Create dictionary (Student, set of course)
info_dict = {}

# Approach - 1
'''
name = set()

for val in range(len(info)):
    name.add(info[val][0])

for name in list(name):
    subj_set = set()
    for val in range(len(info)):
        if info[val][0] == name:
            subj_set.add(info[val][1])
    info_dict.update({
        name : subj_set
    })
print(info_dict)
'''

# Approach - 1
for name, subj in info:
    if info_dict.get(name) == None:
        info_dict.update({
            name : set()
        })
        info_dict[name].add(subj)
    else:
        info_dict[name].add(subj)
print(info_dict)