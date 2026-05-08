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

#My first script used if/elif/else, and my second script used match/case.
#Both scripts solve the problem correctly. I think match/case is easier to read because each department code is clearly listed in its own case.
#I would keep my script simple and make sure I include a default option for invalid department codes.