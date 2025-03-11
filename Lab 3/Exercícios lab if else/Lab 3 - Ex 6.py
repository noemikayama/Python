# Program that reads 2 numbers and, if they are the same, add them; if not, multiply them

a = int(input("\n\n Insert first number: "))
b = int(input("\n\n Insert second nummber: "))

if (a == b):
    c = a + b
else:
    c = a * b

print(f"\n\n\t Final result: {c} \n\n")