# Program to calculate BMI of an individual given it's height and weight
height = float(input("\n Insert your height in meters here: ")) # Gets height in meters
weight = float(input("\n Insert your weight kilograms here: ")) # Gets weight in kilograms
bmi = weight/(height**2) # Calculates bmi = weight/(heightˆ2)
print("\n\n\t Your BMI is: ", bmi) # Prints BMI
print("\n\n *END* \n\n")