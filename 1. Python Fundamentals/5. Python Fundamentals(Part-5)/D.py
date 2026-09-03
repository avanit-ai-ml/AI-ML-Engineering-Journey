# 4. "with" Keyword

with open("sample.txt", "r+") as f:
    print(f.read())

    f.write("I am adding some content in the sample.txt file")