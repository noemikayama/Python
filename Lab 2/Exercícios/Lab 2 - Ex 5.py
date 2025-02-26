# Program that calculates the amount of steps given height of one step and height of the stairs

one_step = float(input("\n Insert height of one step: ")) #Gets height of one step
stairs = float(input("\n Insert height of the stairs: ")) #Gets height of the stairs
num_steps = stairs/one_step #Calculates number of steps
print(f"\n\n\t You will have to climb {num_steps:.0f} steps") #Prints the number of steps that need to be climbed to reach the top
print("\n\n\t\t *END* \n\n")