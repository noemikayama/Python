# Program that gets 2 numbers and shows the smallest

num1 = int(input("\n\n Insert first number: "))
num2 = int(input("\n Insert second number: "))

if (num1 < num2):
    print(f"\n\n\t The smallest number is {num1} \n\n")
else:
    if (num2 < num1):
        print(f"\n\n\t The smallest number is {num2} \n\n")
    else:
        print("\n\n\t Same number \n\n")


