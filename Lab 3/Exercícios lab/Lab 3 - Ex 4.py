# Program that says if a number inserted is positive, null or negative

# Gets the real number
num = float(input("\n Insert number here: "))
# Null number
if (num == 0):
    print("\n\n\t Number is null \n\n")
# Negative number
elif (num < 0):
    print("\n\n\t Number is negative \n\n")
# Positive number
else: 
    print("\n\n\t Number is positive \n\n")
