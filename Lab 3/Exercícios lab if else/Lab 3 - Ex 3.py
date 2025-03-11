# Program that reads 2 numbers and gives you the greatest

num1 = float(input("\n Insert first number: "))
num2 = float(input("\n Insert second number: "))

if (num1 == num2):
    print("\n\n\t Same number \n\n")
elif (num1 > num2):
    print(f"\n\n\t The greatest number is {num1} \n\n")
else:
    print(f"\n\n\t The greatest number is {num2} \n\n")