#How do you convert a temperature from Celsius to Fahrenheit? 

#Input the function wanting to convert 
temperature = float(input("What is the Celsius temperature you are trying to convert? "))

#Setting the Fahrenheit value calculation 
fah_temp = (temperature * (9/5)) + 32

#Print the result 
print(f"The temperature in Fahrenheit is {fah_temp}")
