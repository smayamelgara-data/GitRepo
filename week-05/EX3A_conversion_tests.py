#Exercise 3A Conversion test 
#LAB 1

# Description: This script tests various numeric
# conversion techniques
# Author: Sam Q. Newprogrammer

a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

#Testing Variable A 
float_a = float(a)
int_float_a = int(float(a))

#Slice A
a_sliced = a[1:6]
a_sliced_float = float(a_sliced)

print(a, type(a))
print(float_a, type(float_a))
print(int_float_a, type(int_float_a))
print(a_sliced, type(a_sliced))
print(a_sliced_float, type(a_sliced_float))
print(a.strip())

# Result comments:
# int(a) gives an error because a has a decimal number as a string.
# float(a) works because 101.1 is a decimal number.
# int(float(a)) works because it changes the string to float first, then int.
# strip() removes the spaces before and after the value.

#Variable B
int_b = int(b)
float_b = float(b)

print(b, type(b))
print(int_b, type(int_b))
print(float_b, type(float_b))

# Result comments:
# int(b) works because '55' is a whole number as a string.
# float(b) works and changes it to 55.0.

#Variable C 
# int_c = int(c)  # ValueError: cannot convert because string includes letters
# float_c = float(c)  # ValueError: cannot convert because string includes letters

# slicing numeric part from c
c_sliced = c[0:3]
c_sliced_int = int(c_sliced)

print(c, type(c))
print(c_sliced, type(c_sliced))
print(c_sliced_int, type(c_sliced_int))

# Result comments:
# int(c) gives an error because c has letters after the number.
# float(c) gives an error because c has letters after the number.
# Slicing works because c[0:3] only takes '402'.

#Variable D 
# int_d = int(d)  # ValueError: cannot convert because string includes letters
# float_d = float(d)  # ValueError: cannot convert because string includes letters

# slicing numeric part from d
d_sliced = d[7:8]
d_sliced_int = int(d_sliced)

print(d, type(d))
print(d_sliced, type(d_sliced))
print(d_sliced_int, type(d_sliced_int))
print(d.strip())

# Result comments:
# int(d) gives an error because d has words and a number.
# float(d) gives an error because d has words and a number.
# Slicing works because d[7:8] only takes '5'.
# strip() removes the extra space at the end.
