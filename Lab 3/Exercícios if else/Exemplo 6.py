# Program that identifies if a given integer number can be divided by 5 and 3 simultaneously

# Gets integer number
num = int(input("\n Insert integer number: "))

# Calculates remainders 
div5 = num % 5
div3 = num % 3

if (div5 == 0): # the remainder of the division by 5 is 0
    if (div3 == 0): # the remainder of the division by 5 and 3 are 0
        print("\n\n\t The number can be divided by 3 and 5 \n\n")
    else: # the remainder of the division by 5 is 0 but by 3 is not
        print("\n\n\t The number can only be divided by 5 \n\n")
elif (div3 == 0): # the remaiander of the division by 5 is not 0 and by 3 is
    print("\n\n\t The number can only be divided by 3 \n\n")
else:
    print("\n\n\t The number can't be divided by 5 nor 3 \n\n")

