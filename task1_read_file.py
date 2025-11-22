try:
    file = open("sample.txt", "r")

    print("Reading File content:\n")
    for line in file:
        print(line.strip())

    file.close()

except FileNotFoundError:
    print("Error: File 'sample.txt' does not exist.")
