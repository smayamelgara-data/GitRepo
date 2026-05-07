#How much of your income is withheld for taxes? 

#Setting an income input 
income = float(input("What is your annual income? "))

#Set federal tax percentage 
federal_tax = 0.23

#Calculate monthly dollars
tax_money = (income/12) * federal_tax
 
#Print Results 
print(f"Your monthly withheld tax dollars are {format (tax_money, '.2f')}")

