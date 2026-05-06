#Lab 2: Making calculations with python 

#How do you calculate your net worth given your assets and debts?

#Net worth is assets minus debt

#Assets 
cash = 100
savings = 20000
car_value = 14800

#Debts 
credit_card_debt = 200
student_loan = 8000
car_loan = 12000

#Calculations 
total_assets = cash + savings + car_value 
total_debt = credit_card_debt + student_loan + car_loan
net_worth = total_assets - total_debt 

print("Your total assets are ", total_assets )
print("Your total debt is ", total_debt)
print("Your total net worth is ", net_worth)