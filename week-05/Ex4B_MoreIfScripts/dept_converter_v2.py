#Ex 4B Dept Converter version 2 
#Lab 1 continuation 

# Ask for department code
code = int(input("Enter department code: "))

# Determine department using match/case
match code:
    case 1:
        print("Marketing")
    case 5:
        print("Human Resources")
    case 10:
        print("Accounting")
    case 12:
        print("Legal")
    case 18:
        print("IT")
    case 20:
        print("Customer Relations")
    case _:
        print("Invalid department code")