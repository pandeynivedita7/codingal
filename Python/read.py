# Open the file in read mode
with open('sample.txt', 'r') as file:
    contents = file.read()

# Split the contents into parts (assuming parts are separated by spaces, lines, or some delimiter)
parts = contents.split()  # Default split by spaces; change if needed

# Check if there are at least 5 parts
if len(parts) >= 5:
    print("5th part:", parts[4])  # Index 4 is the 5th element
else:
    print("File does not have 5 parts.")

