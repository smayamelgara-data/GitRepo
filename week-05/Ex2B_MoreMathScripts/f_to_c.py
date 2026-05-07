#How do you convert a temperature from Fahrenheit to Celsius? 

temperature = float(input("What is the Fahrenheit temperature you are trying to convert? "))
#Setting the celsius value calculation 
cel_temp = (temperature -32) * (5/9)

print(f"The temperature in Celsius is {cel_temp}")

