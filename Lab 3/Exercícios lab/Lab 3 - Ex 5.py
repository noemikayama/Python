# Program that gets a number and says if it is a multiple of 5

num = float(input("\n\n Insert a number: "))

if ((num % 5) == 0):
    print(f"\n\n\t {num} is a multiple of 5 \n\n")
else:
    print(f"\n\n\t {num} is not a multiple of 5 \n\n")