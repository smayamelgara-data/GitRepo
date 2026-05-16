#Exercise 2D 
#Lab 1 

# Step 1 & 2
# Create doubler lambda function

doubler = lambda n: n * 2

# Step 3
# Test doubler

print(doubler(8))
print(doubler(-4))
print(doubler('banana'))


# Step 4
# Create tripler lambda function

tripler = lambda n: n * 3

# Test tripler

print(tripler(8))
print(tripler(-4))
print(tripler('banana'))


# Step 5
# Create a function that returns a multiplier lambda

def multiplier(x):
    return lambda n: n * x


# Create variables using multiplier()

quadrupler = multiplier(4)
quintupler = multiplier(5)
sextupler = multiplier(6)
septupler = multiplier(7)
octupler = multiplier(8)
nonupler = multiplier(9)
decupler = multiplier(10)


# Step 6
# Test each new variable

print(quadrupler(2))
print(quintupler(2))
print(sextupler(2))
print(septupler(2))
print(octupler(2))
print(nonupler(2))
print(decupler(2))