#Exercise 4A If Basics 
#Lab 1 

x = 100
y = 20

#Division statement 
if x / y == 5:
    print("x divided by y is 5")
    x = 1
else:
    print("are the variables set up correctly?")

#Multiplication statement
if x * y == y:
    print("now x times y is y")
    x = 10
else:
    print("Whoops, x equals", x)


#Less than operation statement 
if x < y:
    print("x is less than y")
    x = x * 2
else:
    print("uh oh, x is not less than y")

#Greater than operation statement 
if x > y:
    print("how is x greater than y??")
else:
    print("x is NOT greater than y")

#Final Print statement 
print("The final value of x is", x, "and the final value of y is", y)
