# Program that gets N numbers and gives the greates and the smallest

N = int(input("\n\n Insert how many numbers you want to evaluate: "))

i = 1
great = 0

num1 = int(input("\n\n Enter number: "))
great = num1
small = num1

while (i <= (N - 1)):  
    num2 = int(input("\n\n Enter number: "))
    if (num2 >= great):
        great = num2
    elif (small >= num2):
        small = num2
    i = i + 1

print(f"\n\n\t The smallest number is {small} and the greatest is {great} \n\n")