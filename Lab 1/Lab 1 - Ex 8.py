# PRogram that calculates prizes based on the given total of all of them
prize = float(input("\n Insert total amount of the prize here (R$): ")) # Gets total amount of the prize
first = 0.46 * prize # Calculates first place (46%)
second = 0.32 * prize # Calculates second place (32%)
third = prize - first - second # Calculates third place (rest)
print("\n\n\t THE PRIZES ARE: ") 
print("\n\t\t First place: R$", first) # Prints first place
print("\n\t\t Second place: R$", second) # Prints second place
print("\n\t\t Third place: R$", third) # Prints third place
print("\n\n *END* \n\n")