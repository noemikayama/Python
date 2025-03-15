# Program that gets 3 numbers and shows the smallest

num1 = int(input("\n\n Insert first number: "))
num2 = int(input("\n\n Insert second number: "))
num3 = int(input("\n\n Insert third number: "))

if (num1 == num2 and num2 == num3):
    menor = num1
    print("\n\n\t Same number \n")
else:
    if (num1 < num2):
        menor = num1
    else: 
        menor = num2
    if (num3 < menor):
        menor = num3

print(f"\n\n\t Smallest number is {menor} \n\n")

