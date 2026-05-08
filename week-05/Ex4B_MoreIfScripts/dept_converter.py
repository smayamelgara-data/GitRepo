#Exercise 4B Dept Converter 
#Lab 1 

# Ask for department code
code = int(input("Enter department code: "))

# Determine department
if code == 1:
    print("Marketing")
elif code == 5:
    print("Human Resources")
elif code == 10:
    print("Accounting")
elif code == 12:
    print("Legal")
elif code == 18:
    print("IT")
elif code == 20:
    print("Customer Relations")
else:
    print("Invalid department code")

    