# Create a file and write content to it

file = open("sample.txt", "w")   # "w" = write mode

file.write("Hello, this is a sample file.\n")
file.write("This file was created using Python.\n")

file.close()

print("File created and content written successfully.")