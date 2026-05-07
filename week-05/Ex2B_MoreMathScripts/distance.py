#How do you calculate distance between coordinates 

#Input coordinates 
x1, y1 = map(float, input("Enter point 1 (in format:x y): " ).split())
x2, y2 = map(float, input("Enter point 2 (in format: x y): " ).split())

#Calculate distance 
distance = (((x2 -x1)**2)+((y2-y1)**2)) ** 0.5

print(f"The distance between the points is {format (distance, '.2f')}")



