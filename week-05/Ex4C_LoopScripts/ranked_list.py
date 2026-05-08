#Exercise 4C Ranked list 
#Lab 3 

# Create a list
foods = ["tacos", "ramen", "jerk chicken", "pizza", "sushi"]

# Print numbered list
for index, food in enumerate(foods, start=1):

    # Check if it is the first item
    if index == 1:
        print(index, ".", food, "<- top pick!")

    else:
        print(index, ".", food)

print()

# BONUS: Reverse order
print("Reverse Order:")

reversed_foods = list(reversed(foods))

for index, food in enumerate(reversed_foods, start=1):
    print(index, ".", food)

    