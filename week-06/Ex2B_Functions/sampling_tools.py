#Ex2B Using Library Functions 
#Lab 1 

import random

products = ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam',
'Headset', 'Docking Station', 'USB Hub', 'Desk Lamp', 'Surge Protector']


# 4a: Product of the Day
product_of_day = random.choice(products)
print("Product of the Day:", product_of_day)

# 4b: Select 3 products without repeats
survey_products = random.sample(products, 3)
print("Survey products:", survey_products)

# 4c: Shuffle all products
random.shuffle(products)
print("Shuffled products:", products)

# 4d: Random daily transaction count
transactions = random.randint(50, 300)
print("Daily transaction count:", transactions)
