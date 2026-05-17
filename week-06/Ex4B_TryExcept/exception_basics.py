#Exercise 4B 
#Lab 1 

# ValueError Example

try:
    age = int("hello")

except ValueError:
    print("ValueError: You entered something that cannot be converted into a number.")

else:
    print(age)

finally:
    print("Let's try another one...\n")


# Another ValueError Example

try:
    number = float("banana")

except ValueError:
    print("ValueError: Python could not convert the text into a decimal number.")

else:
    print(number)

finally:
    print("Let's try another one...\n")


# NameError Example

try:
    m = banana

except NameError:
    print("NameError: Oops, looks like you tried to use an undefined variable.")

else:
    print(m)

finally:
    print("Let's try another one...\n")


# Another NameError Example

try:
    print(score)

except NameError:
    print("NameError: The variable does not exist.")

else:
    print(score)

finally:
    print("Let's try another one...\n")


# TypeError Example

try:
    result = "5" + 10

except TypeError:
    print("TypeError: You cannot combine a string and an integer.")

else:
    print(result)

finally:
    print("Let's try another one...\n")


# Another TypeError Example

try:
    total = len(100)

except TypeError:
    print("TypeError: len() only works with collections or strings.")

else:
    print(total)

finally:
    print("Let's try another one...\n")


# SyntaxError Example

try:
    eval("if 5 > 2 print('hello')")

except SyntaxError:
    print("SyntaxError: Python found invalid syntax in the code.")

else:
    print("No syntax errors found.")

finally:
    print("Let's try another one...\n")


# Another SyntaxError Example

try:
    eval("x === 5")

except SyntaxError:
    print("SyntaxError: Python does not recognize this operator.")

else:
    print("No syntax errors found.")

finally:
    print("Let's try another one...\n")
    