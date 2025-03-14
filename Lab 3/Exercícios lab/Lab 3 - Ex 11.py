# Program that calculates x and y given the system

print("\n\n a*x + b*y = c \n d*x + e*y = f")
a = int(input("\n\n Insert a: "))
b = int(input("\n\n Insert b: "))
c = int(input("\n\n Insert c: "))
d = int(input("\n\n Insert d: "))
e = int(input("\n\n Insert e: "))
f = int(input("\n\n Insert f: "))

while (a != 0 or b != 0 or c != 0 or d != 0):
    if ((a*e - b*d) == 0):
        print("\n\n Denominator = 0 -> ERROR")

    else:
        x = ((c*e) - (b*f))/(a*e - b*d)
        y = ((a*f) - (c*d))/(a*e - b*d)
        if (x < 0 or y < 0):
            print("\n\n\t No solution! ")
        else:
            print(f"\n\n\t x = {x} and y = {y}")
            a = int(input("\n\n Insert a: "))
            b = int(input("\n\n Insert b: "))
            c = int(input("\n\n Insert c: "))
            d = int(input("\n\n Insert d: "))
            e = int(input("\n\n Insert e: "))
            f = int(input("\n\n Insert f: "))
else: 
    print("\n\n\t *END* \n\n")