#Exercise 4B Complex taxes
#Lab 3 

# Get input 
pay_rate = float(input("Enter pay rate: "))
hours_worked = float(input("Enter hours worked: "))
filing_status = input("Enter filing status (single or joint): ")

# Weekly gross pay 
if hours_worked <= 40:
    gross_pay = pay_rate * hours_worked
else:
    overtime_hours = hours_worked - 40
    gross_pay = (pay_rate * 40) + (overtime_hours * pay_rate * 1.5)

# Annual pay
annual_pay = gross_pay * 52

# Determine tax rate
if filing_status == "single":
    if annual_pay < 12000:
        tax_rate = 0.05
    elif annual_pay <= 24999.99:
        tax_rate = 0.10
    elif annual_pay <= 74999.99:
        tax_rate = 0.15
    else: 
        tax_rate =0.20 

elif filing_status == "joint":
    if annual_pay < 12000:
        tax_rate = 0.00
    elif annual_pay <= 24999.99: 
        tax_rate = 0.06
    elif annual_pay <= 74999.99: 
        tax_rate = 0.11
    else: 
        tax_rate =0.20

else:
    print("Invalid filing status")
    tax_rate = 0

# Weekly tax + net pay
tax_withheld = gross_pay * tax_rate
net_pay = gross_pay - tax_withheld

# Output
print("You worked", hours_worked, "hours this period.")
print("Because you earn $" + format(pay_rate, ".2f") + " per hour, your gross weekly pay is $" + format(gross_pay, ".2f"))
print("Your filing status is", filing_status)
print("Your tax withholding for the week is $" + format(tax_withheld, ".2f"))
print("Your net pay is $" + format(net_pay, ".2f"))

