# Task: This program opens a file named "data.txt" and reads its contents.
# Modify the code and use exception handling to handle the case where the file does not exist.

# Hint: Use try-except to catch FileNotFoundError.

myFile = open('data.txt', 'r') # Opens the file for read

content = myFile.read() # Reads the content of the file
print(content)

myFile.close() # Always close the file when we are done with it
