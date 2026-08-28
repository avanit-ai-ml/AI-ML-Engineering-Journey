# 6. Using Loops with Lists

marks = [90, 94, 93, 97, 98, 95]

idx = 0
target = 90
for val in marks:
    if val == target:
        print(f"{target} is at Index: {idx}")
    elif idx == len(marks)-1:
        print(f"{target} is at not in List")
    else:
        idx += 1