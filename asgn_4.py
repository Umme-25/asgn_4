#Assignment
###task 1

try:
    with open("t_asgn\\sample.txt",'r') as file:
         print("Reading the file.")
         for i, line in enumerate(file, start=1):
            print(f"Line {i}: {line.strip()}")

except FileNotFoundError:
    print("Error: The file 'sample.txt' is not present")

###Task 2

# Step 1: Take user input and write to file
data1 = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(data1 + "\n")

print("Data successfully written to output.txt.\n")

# Step 2: Take more input and append to the file
data2 = input("\nEnter additional text to append: ")

with open("output.txt", "a") as file:
    file.write(data2 + "\n")

print("Data successfully appended.")

# Step 3: Read and display the final content
print("\nFinal Content of output.txt")
with open("output.txt", "r") as file:
    content = file.read()
    print(content)

