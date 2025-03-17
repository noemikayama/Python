num = int(input("\n\n Insert number: "))
prime = 0
i = 1

while (i <= num):
    if (num % i == 0):
        print(f"\n\n Can be divided by {i} \n\n")
    elif (num % i != 0 and i != 1 and i != num):
        prime = prime + 1
    i = i + 1

if (prime == (num - 2)):
    print("\n\n\t Prime number \n\n")
else: 
    print("\n\n\t Regular number \n\n")
