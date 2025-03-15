# Program that gives you the smallest number out of 100 numbers

count = 0
small = 99

while (count < 100):
    num = int(input("\n\n Insert number: "))
    if (num < small):
        small = num
    count = count + 1

print(f"\n\n\t Smallest is: {small} \n\n")

