#Exercise 3A Classes 
#Lab 1: Restaurants 

class Restaurant:
    '''
    This class represents a restaurant and stores
    the restaurant name and type of food served.
    '''

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type

    def describe_rest(self):
        print(self.rest_name, "serves", self.food_type + ".")

    def rest_open(self):
        print(self.rest_name, "is open.")


# Create restaurant instances

wendys = Restaurant("Wendy's", "fast food")
dunkin = Restaurant("Dunkin Donuts", "coffee and donuts")
taco_baco = Restaurant("Taco Baco", "Mexican food")


# Call methods for Wendy's

wendys.describe_rest()
wendys.rest_open()

print()


# Call methods for Dunkin Donuts

dunkin.describe_rest()
dunkin.rest_open()

print()


# Call methods for Taco Baco

taco_baco.describe_rest()
taco_baco.rest_open()