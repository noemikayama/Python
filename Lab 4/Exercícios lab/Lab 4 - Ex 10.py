num = int(input("\n\n Insert number: "))

while (num >= 0):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * (num - (num - i))
    print(f"\n\n\n {num}! = {fact} \n\n")
    num = int(input("\n\n Insert number: "))

print("\n\n\t *END OF THE PROGRAM* \n\n")