#Exercise 3A String Cleaning 
#LAB 2 

# Original messy data
name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"

salary_1 = "$82,500"
salary_2 = "$74,000"

# 3. Convert names to lowercase

print(name_1.lower())
print(name_2.lower())
print(name_3.lower())

# 4. Convert names to title case

print(name_1.title())
print(name_2.title())
print(name_3.title())


# 5. Remove $ from salaries

clean_salary_1 = salary_1.replace("$", "")
clean_salary_2 = salary_2.replace("$", "")

print(clean_salary_1)
print(clean_salary_2)

# Check type
print(type(clean_salary_1))
print(type(clean_salary_2))


# 6. Chain replace() and int()

salary_1_int = int(salary_1.replace("$", "").replace(",", ""))

print(salary_1_int)
print(type(salary_1_int))

