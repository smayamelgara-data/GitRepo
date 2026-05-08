#Exercise 4C Sales Performance 
#Lab 4

# Create the sales data list
sales_data = [
    ('Marcus Webb', 'East', 4250.00),
    ('Priya Sharma', 'West', 5875.50),
    ('DeShawn Carter', 'East', 3100.75),
    ('LaTonya Rivers', 'South', 6420.00),
    ('Bob Nguyen', 'West', 4980.25),
]

# Variable to track total sales
total_sales = 0

# Loop through each tuple
for name, region, sales in sales_data:

    # Print summary line
    print(name, "(" + region + "): $" + format(sales, ",.2f"))

    # Check for top performer
    if sales > 5000:
        print("^ Top performer!")

    # Add sales to total
    total_sales = total_sales + sales

# BONUS Print overall total
print()
print("Overall Sales Total: $" + format(total_sales, ",.2f"))

