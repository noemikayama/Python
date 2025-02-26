# Program that calculates cost of placing screen on a property

length = float(input("\n Insert length (m): ")) #Gets measurment of one side
width = float(input("\n Insert width (m): ")) #Gets measurment of the other side
screen = float(input("\n Insert price of 1 m of screen (R$): ")) #Gets the price of 1m of screen
perimeter = 2*length + 2*width #Calculates the perimeter 
total_screen = perimeter*screen #Calculates total cost
print(f"\n\n\t It will cost R${total_screen:.2f}") #Prints total cost
print("\n\n\t\t *END* \n\n") 
