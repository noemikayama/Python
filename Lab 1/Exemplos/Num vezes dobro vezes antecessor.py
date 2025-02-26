# Program to read and multiply it's double to the number before
num = int(input("\n Insert integer number here: ")) # Get integer number
res = 2 * num * (num - 1) # Calculates 2*num*(n-1)
print("\n\n 2 x ", num, " x (", num, "- 1) = ", res) # Prints the expression
print("\n\n *END* \n\n")