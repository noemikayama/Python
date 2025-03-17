first = int(input("\n\n Insert number: "))
num = int(input("\n Insert number: "))

if (num > first) :
    second = first
    first = num
else:
    second = num

for count in range(0, 2):
    num = int(input("\n Insert number: "))
    if (num > first):
        second=first
        first = num
    elif (num > second):
        second = num

print(f"\n\n\t The 2 greatest numbers are {first} and {second} \n\n")