#How long will it take a savings account worth X to double in value based on an interest rate of IR?

# Example values
current_savings = 1200
interest_rate = 0.06

# Calculations
doubled_balance = current_savings * 2
years = 72 / (interest_rate * 100)

# Output
print("Your current savings is", current_savings)
print("At a " + format(interest_rate, ".0%") + " interest rate, your savings account will be")
print("worth $" + format(doubled_balance, ".2f") + " in " + format(years, ".1f") + " years")
