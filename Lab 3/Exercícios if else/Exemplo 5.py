num1 = float(input("\n Insert first number here: "))
num2 = float(input("\n Insert second number here: "))
num3 = float(input("\n Insert third number here: "))
if (num1 > num2):
    if (num1 > num3):
        print(f"\n\n\t Highest number is {num1:.1f} \n\n")
    else:
        print(f"\n\n\t Highest number is {num3:.1f} \n\n")
else:
    if(num2 > num3):
        print(f"\n\n\t Highest number is {num2:.1f} \n\n")
    else:
        print(f"\n\n\t Highest number is {num3:.1f} \n\n")
        
          