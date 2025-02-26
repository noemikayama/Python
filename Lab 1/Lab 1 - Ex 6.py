# Program that calculates the cost of covering an area with carpet given sides of the room and the price of one square meter of carpet
side1 = float(input("\n Insert first side of the room: ")) # Gets measurments of the first side of the room
side2 = float(input("\n Insert second side of the room: ")) # Gets measurments of the second side of the room
m2_price = float(input("\n Insert the price of a square meter of carpet: ")) # Gets price of one sqare meter of carpet
total = side1 * side2 * m2_price # Calculates the toatl price to cover the room with carpet (area * m2_price)
print("\n\n\t The total cost of the carpet will be (R$): ", total) # Prints the total cost to cover room with carpet
print("\n\n *END* \n\n")