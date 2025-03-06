# Program to convert Fahrenheit in Celsius

fahrenheit = float(input("\n Insert temperature in degrees Fahrenheit: ")) # Get degrees in Fahrenheit
celsius = ((fahrenheit - 32)*5)/9 # Calculates conversion
print(f"\n\n\t {fahrenheit:^6.2f} degrees Fahrenheit is {celsius:^6.2f} degrees Celsius") # Prints degrees
print("\n\n\t\t *END* \n\n")
