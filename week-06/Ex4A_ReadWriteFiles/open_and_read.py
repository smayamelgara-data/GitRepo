# Open about_me.txt in read mode
f = open("about_me.txt", "r")

# First variable: read first 50 characters
first_50_characters = f.read(50)

# Second variable: read the next four lines into a list
next_four_lines = []

for i in range(1, 5):
    next_four_lines.append(f.readline())

# Third variable: read the next 100 characters, rounded up to complete lines
next_100_characters = f.readlines(100)

# Print the results
print("First 50 characters:", first_50_characters)

print("Next four lines, as list by line:", next_four_lines)

print("Next 100 characters, as list by line, rounded up to complete lines:", next_100_characters)

# Close the file
f.close()