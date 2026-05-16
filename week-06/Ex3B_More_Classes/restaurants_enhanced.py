class Restaurant:
    '''
    This class represents a restaurant and stores
    the restaurant name, type of food, number of customers served,
    and customer ratings.
    '''

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []

    def describe_rest(self):
        print(self.rest_name, "serves", self.food_type + ".")

    def rest_open(self):
        print(self.rest_name, "is open.")

    def add_num_served(self):
        customers = int(input("How many customers served today? "))
        self.number_served = self.number_served + customers

    def print_num_served(self):
        print(self.rest_name, "has served", self.number_served, "customers")

    def customer_rating(self):
        while True:
            rating_input = input("How would you rate your experience today on a scale of 1-5? ")

            if rating_input.isdigit():
                rating = int(rating_input)

                if rating >= 1 and rating <= 5:
                    self.customer_ratings.append(rating)

                    average = sum(self.customer_ratings) / len(self.customer_ratings)

                    print("Your rating was", rating)
                    print("The average rating for this restaurant is", average)
                    break

                else:
                    print("Please enter a number between 1 and 5.")

            else:
                print("Please enter a whole number between 1 and 5.")


# Create restaurant instances

wendys = Restaurant("Wendy's", "fast food")
dunkin = Restaurant("Dunkin Donuts", "coffee and donuts")
taco_baco = Restaurant("Taco Baco", "Mexican food")


# Test number served

wendys.print_num_served()
wendys.add_num_served()
wendys.add_num_served()
wendys.print_num_served()

print()

dunkin.print_num_served()
dunkin.add_num_served()
dunkin.add_num_served()
dunkin.print_num_served()

print()

taco_baco.print_num_served()
taco_baco.add_num_served()
taco_baco.add_num_served()
taco_baco.print_num_served()

print()


# Test customer ratings

wendys.customer_rating()
wendys.customer_rating()
wendys.customer_rating()

print()

dunkin.customer_rating()
dunkin.customer_rating()
dunkin.customer_rating()

print()

taco_baco.customer_rating()
taco_baco.customer_rating()
taco_baco.customer_rating()