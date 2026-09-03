# 2. Operations on Files

# ------------ Read Operations ------------
f = open("data.txt", "r")

# data = f.read()
data = f.readline()

print(data)

f.close()

# ------------ Write Operations ------------
f = open("data.txt", "w")

f.write("New data addeding!...")

f.close()


f = open("data.txt", "r")

data = f.read()

print(data)

f.close()