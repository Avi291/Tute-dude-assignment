# Open file in read mode

file = open("sample.txt", "r")   # "r" = read mode

content = file.read()            # Read entire file
print(content)                   # Display content

file.close()