#How do you calculate the tip amount on a restaurant bill given the tip percentage?

# Example values
bill1 = 40
tip_percent1 = 20

# Calculate tip
tip1 = bill1 * (tip_percent1 / 100)

# Output
print("The tip on a $" + str(bill1) + " restaurant bill is $" + str(tip1))

#Lab 3: Inserting the Input() function within the tip_amount script 

bill = float(input("What is your total bill today? "))
tip_percent = float(input("What is the tip percentage you would like to pay? "))

tip = bill * (tip_percent / 100)

print("The tip on a $" + str(bill) + " restaurant bill is $" + str(tip))

#Possible pitfalls are going to be the conversion of the number, i assigned it to be a float but it could be a strict int. 
