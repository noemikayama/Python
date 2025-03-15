# Program that giver you the smallest number out of 100 numbers

cont = 1
small = int(input("\n\n Insert number: "))

while (cont < 5):
    num = int(input("\n Insert number: "))
    if (num < small):
        small = num
    cont = cont + 1

print(f"\n\n\t Smallest is: {small} \n\n")

