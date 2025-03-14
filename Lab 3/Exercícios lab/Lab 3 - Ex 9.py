# Program that prints multiples of 7 between 100 and 470

num1 = 100
num2 = 450

print("\n\n MULTIPLES OF 7 BETWEEN 100 AND 470: \n\n")
while(num2 >= num1):
    if ((num1 % 7) == 0): #Multiple of 7
        print(num1)
        num1 = num1 + 1
    else:
        num1 = num1 + 1
else:
    print("\n\n Out of range \n\n")
