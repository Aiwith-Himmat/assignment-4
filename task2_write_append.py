# Taking input to write in the file
text = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(text + "\n")

print("Data successfully written to output.txt.\n")


# Taking input to append
additional_text = input("Enter additional text to append: ")

with open("output.txt", "a") as file:
    file.write(additional_text + "\n")

print("Data successfully appended.\n")


# Reading final content
print("Final content of output.txt:\n")

with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
