# Program to read an integer number and calculate the difference between it's triple and the double of the it's following number
num = int(input("\n Insert integer number: ")) # Get integer number
res = (3 * num) - (2 * (num -1)) # Calculates (3*n) - (2*(n-1))
print("\n\n\t ( 3 * ", num, ") - ( 2 * (", num, "- 1 )) = ", res) # Prints expression and result
print("\n\n *END* \n\n")