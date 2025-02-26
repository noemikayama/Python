# Program that calculates economy rate af a car during a given travel
km = float(input("\n Insert kilometers travelled (km): ")) # Gets kilometers travelled
liters = float(input("\n Insert consumed liters of fuel (L): ")) # Gets liters used
consumes = km/liters # Calculates how much the car consumes in km/L
print("\n\n\t The economy rate in of this car is: ", consumes, "km/L") # Prints car's economy rate
print("\n\n *END* \n\n")