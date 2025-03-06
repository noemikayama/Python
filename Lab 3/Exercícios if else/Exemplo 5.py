# Program that determines greater number out of 3 given numbers

num1 = float(input("\n Insert first number here: "))
num2 = float(input("\n Insert second number here: "))
num3 = float(input("\n Insert third number here: "))
if (num1 > num2):
    if (num1 > num3): #num1>num2 and num1>3
        print(f"\n\n\t Highest number is {num1} \n\n")
    else: #num1>num2 and num3>num1
        print(f"\n\n\t Highest number is {num3} \n\n")
else:
    if(num2 > num3): #num1<num2 and num2>num3
        print(f"\n\n\t Highest number is {num2} \n\n")
    else: #num1<num2 and num3>num2
        print(f"\n\n\t Highest number is {num3} \n\n")
        
          