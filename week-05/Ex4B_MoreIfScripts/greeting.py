#Exercise 4B Greetings 
#Lab 2 

# Create a variable for the current hour
# Use numbers from 0 to 23
hour = 12

# Check the hour and print the correct greeting
if hour >= 23 or hour < 4:
    print("What are you doing up so late??")
elif hour < 10:
    print("Good morning!")
elif hour < 17:
    print("Good day!")
else:
    print("Good evening!")

    