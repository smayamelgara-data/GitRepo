#Exercise 4B Min & Max Calculations 
#Lab 4 

# Assign values
a = 55
b = 78
c = 12

# Find smallest
if a <= b and a <= c:
    smallest = a
elif b <= a and b <= c:
    smallest = b
else:
    smallest = c

# Find largest
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

# Output
print("The smallest number is", smallest)
print("The largest number is", largest)

