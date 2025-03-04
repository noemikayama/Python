# Program that calculates value of y from x value according to:
#           y = x  if  x < 1
#           y = 0  if  x = 1
#           y = x^2  if  x > 1

# Gets number
x = float(input("\n Insert number: "))
if (x < 1):
    y = x
elif (x == 1):
    y = 0
else:
    y = x ** 2
print(f"\n\n\t So x = {x:.2f} and y = {y:.2f} \n\n")