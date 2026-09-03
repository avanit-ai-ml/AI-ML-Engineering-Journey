# 6. Practice Problem
line = 1
with open("practice_problem_file.txt", "r") as f:
    while True:
        data = f.readline()
        if "Python" in data:
            print(f"Line number: {line}")
            break
        elif data == "":
            print("Not present")
            break
        else:
            line += 1
