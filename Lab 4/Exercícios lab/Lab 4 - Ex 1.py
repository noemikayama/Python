# Program that reads a number and tells you where it is located

num = int(input("\n\n Insert number: "))

while (num >= 0):
    if (num <= 25):
        print("\n\n\t Number between 0 and 25 \n")
    elif (num <= 50):
        print("\n\n\t Number is between 26 and 50 \n")
    elif (num <= 75):
        print("\n\n\t Number is between 51 and 75 \n")
    elif (num <= 100):
        print("\n\n\t Number is between 76 and 100 \n")
    else:
        print("\n\n\t Number out of range \n")
    num = int(input("\n\n Insert number: "))

print("\n\n\t * END OF PROGRAM * \n\n")