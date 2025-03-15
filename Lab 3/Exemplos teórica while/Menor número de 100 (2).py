# Program that giver you the smallest number out of 100 numbers

count = 1
small = int(input("\n\n Insert number: "))

while (count < 100):
    num = int(input("\n Insert number: "))
    if (num < small):
        small = num
    count = count + 1

print(f"\n\n\t Smallest is: {small} \n\n")

