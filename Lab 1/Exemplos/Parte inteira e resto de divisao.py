# Program that prints the integer part of a division and the remainder of the same division
# Division: dividend/divisor = quotient + remainder

num1 = int(input("\n Insert the dividend: ")) # Get the dividend of the division
num2 = int(input("\n Insert the divisor: ")) # Get the divisor of the division
integer = num1 // num2 # Calcultes the integer part of the quotient
rem = num1 % num2 # Calculates the remainder of the division

print("\n\n The division is:", num1, "/", num2) # Prints the division
print("\n\t The integer part of the quotient is: ", integer) # Prints the integer part of the quotient
print("\n\t The remainder is: ", rem) # Prints the remainder of the division
print("\n\n *END* \n\n")


