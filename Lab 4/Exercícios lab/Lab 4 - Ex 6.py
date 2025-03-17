numerator = 1
denominator = 1
S = 0
print("\n\n S = ")


while (numerator <= 10):
    if (numerator % 2 == 0):
        den = - (denominator**2)
    else:
        den = (denominator**2)
    S = S + (numerator/denominator)
    print(f"{numerator}/{den} + ", end=" ")
    numerator = numerator + 1
    denominator = denominator + 1

print(f"\n\n\t S = {S} \n\n")