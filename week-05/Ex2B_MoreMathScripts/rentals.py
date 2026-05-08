#There are X people going on a tour. Charter vans seat 15 passengers each. Vans cost
#$250 per day to rent (including the driver’s pay). How many vans do you need? How
#much will it cost to rent vans? What is the cost if you split it per person?

# Rentals calculation
people = int(input("How many people are going on the tour? "))

# Calculate vans needed
vans_needed = people // 15

if people % 15 != 0:
    vans_needed = vans_needed + 1

# Cost calculations
total_cost = vans_needed * 250
cost_per_person = total_cost / people

# Output
print("Vans needed:", vans_needed)
print("Total cost:", total_cost)
print("Cost per person:", format(cost_per_person, ".2f"))# Rentals calculation

people = int(input("How many people are going on the tour? "))

# Calculate vans needed
vans_needed = people // 15

if people % 15 != 0:
    vans_needed = vans_needed + 1

# Cost calculations
total_cost = vans_needed * 250
cost_per_person = total_cost / people

# Output
print("Vans needed:", vans_needed)
print("Total cost:", total_cost)
print("Cost per person:", format(cost_per_person, ".2f"))
