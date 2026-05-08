#Exercise 4D BONUS Number Guesser Game 
#Simple game that generates a random interger and makes the user guess the interger 

# Import shuffle
from random import shuffle

# Create a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Shuffle the list
shuffle(numbers)

# Pick the first number after shuffling
secret_number = numbers[0]

# Create a list to store guesses
guessed_numbers = []

# Track number of guesses
guess_count = 0

# Show the range
print("Guess a number between 1 and 10")

# Start loop
while True:

    # Get user input
    user_guess = input("Enter your guess: ")

    # Check if input is a number
    if user_guess.isdigit():

        # Convert to integer
        user_guess = int(user_guess)

        # Add guess to list
        guessed_numbers.append(user_guess)

        # Increase guess counter
        guess_count = guess_count + 1

        # Check the guess
        if user_guess < secret_number:
            print("Higher")

        elif user_guess > secret_number:
            print("Lower")

        else:
            print("Correct! You guessed the number!")

            # Show total guesses
            print("Total guesses:", guess_count)

            # Show all guessed numbers
            print("Your guesses were:", guessed_numbers)

            # Bonus message
            if guess_count < 5:
                print("You're awesome!")

            # End loop
            break

    else:
        print("Please enter a valid number.")

        