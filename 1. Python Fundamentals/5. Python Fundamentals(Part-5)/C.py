# 3. Modes in File Operations

# Note:- Read & Write already completed

# ------------ x - Mode ------------
f = open("xmodedata.txt", "x")

f.write("X mode inforation.")

f.close()


# ------------ a - Mode ------------

f = open("xmodedata.txt", "a")

f.write("\nAppending new information at the end of the existing data...")

f.close()