# Program that says if the inserted number is odd or even

# Gets the number
num = int(input("\n Insert integer number: "))
# Calculates the remainder of the number when you divide it by 2
remainder = num % 2
# Remainder is 0 -> even
if (remainder == 0):
    print("\n\n\t Number is even \n\n")
# Remainder is 1 -> odd
else:
    print("\n\n\t Number is odd \n\n")