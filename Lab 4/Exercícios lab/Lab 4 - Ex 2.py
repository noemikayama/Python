num = int(input("\n\n Insert a number: "))

print(f"\n\n\t Numbers until {num} that can be divided by 4 \n")

for count in range(1, num + 1):
    if ((count % 4) == 0):
        print(count, end= " ")

print("\n\n\t * END OF THE PROGRAM * \n\n")