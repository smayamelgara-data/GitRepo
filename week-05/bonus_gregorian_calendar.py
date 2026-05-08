#Bonus lab from Exercise 4A 

# Ask user for a year
year = int(input("Enter a year: "))

# Check if it is a leap year
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a leap year")
        else:
            print(year, "is NOT a leap year")
    else:
        print(year, "is a leap year")
else:
    print(year, "is NOT a leap year")

    