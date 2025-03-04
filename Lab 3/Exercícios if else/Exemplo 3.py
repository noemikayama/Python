# Program that says if a number inserted is positive, null or negative

# Gets the real number
num = float(input("\n Insert number here: "))
# Negative number
if (num < 0):
    print("\n\n\t Number is negative \n\n")
# Null number
elif (num == 0):
    print("\n\n\t Number is null \n\n")
# Positive number
elif (num > 0):
    print("\n\n\t Number is positive \n\n")
# Invalid number
else:
    print("\n\n\t Number is invalid \n\n")