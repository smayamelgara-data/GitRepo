#Exercise 3B Candy Store 
#Lab 2 

# Create tuples
candies = ("Blow Pops", "Jolly Ranchers", "Airheads")
flavors = ("Cherry", "Blueberry", "Green Apple")

# Create a set for combinations
candy_combos = set()

# Add combinations using index
candy_combos.add(candies[0] + " - " + flavors[0])  # Blow Pops - Cherry
candy_combos.add(candies[1] + " - " + flavors[1])  # Jolly Ranchers - Blueberry
candy_combos.add(candies[2] + " - " + flavors[2])  # Airheads - Green Apple

# Output
print("Today's candy options include:")
print(candy_combos)

# Print multiple times
print(candy_combos)
print(candy_combos)