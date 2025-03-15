# Program that giver you the smallest number out of 100 numbers

cont = 0
small = 99

while (cont < 100):
    num = int(input("\n\n Insert number: "))
    if (num < small):
        small = num
    cont = cont + 1

print(f"\n\n\t Smallest is: {small} \n\n")

