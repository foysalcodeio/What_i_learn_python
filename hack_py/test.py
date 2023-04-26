# read and write to files
file_open = open("readme.txt", "r")
for line in file_open:
    print(line.strip("\n"))
    if line.strip("\n") == "rad 4":
        print("last line")