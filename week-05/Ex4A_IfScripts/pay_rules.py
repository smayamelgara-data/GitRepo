#Exerice 4A Payment Rules
#Lab 2 

# Get input
pay_rate = float(input("Enter pay rate: "))
hours_worked = float(input("Enter hours worked: "))

# Calculate gross pay
if hours_worked <= 40:
    gross_pay = pay_rate * hours_worked
else:
    overtime_hours = hours_worked - 40
    gross_pay = (pay_rate * 40) + (overtime_hours * pay_rate * 1.5)

# Output
print("Gross pay is", format(gross_pay, ".2f"))