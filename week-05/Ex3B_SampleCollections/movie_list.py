# Ex 3B Sample Collections : Movie List 
# Lab 1

#Create a movie list 
movies = ["The Grinch", "Real Steel", "The Lorax", "The Bee Movie", "Twilight"]

#Using len() and print the list 
print(f"This list of movies includes my top {len(movies)} favorite movies!")
print(movies)

#Using sorted()
print(sorted(movies))   # temporary sorted version

#Sorted does not change the original list just reaaranges it 

#Using sort()
movies.sort()
print(movies)

#Sort() permanetly changes the original list 

#Using append() to add a new movie 
movies.append("Monsters Inc")

print(f"This list of movies includes my top {len(movies)} favorite movies!")
print(movies)

