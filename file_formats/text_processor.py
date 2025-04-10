
with open("notes.txt", "w") as file:
    file.write("Python script is a file that generally contains a short self - contained set of instructions\n")
    file.write("File handling is simplified with built-in methods.\n")


with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())
