# Program that calculates amount of liters that a car uses

economy_rate = 12 #Economy rate is 12 km/L
speed = float(input("\n Insert average speed: ")) #Gets speed
time = float(input("\n Insert duration of the trip: ")) #Gets time in hours
distance = speed*time #Calculates distance of the trip
liters = distance/economy_rate #Calculates amount of fuel used in liters
print(f"\n\n - Average speed: {speed:.2f} km/h") #Prints average speed in km/h
print(f"\n\n - Time: {time:.2f} hours") #Prints duration of the trip in hours
print(f"\n\n - Distance: {distance:.2f} km") #Prints distance of the trip in km
print(f"\n\n - Amount of liters of fuel: {liters:.2f} L") #Prints liters used
print("\n\n\t\t *END* \n\n")