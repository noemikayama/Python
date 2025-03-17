denominator = 1
S = 0

for numerator in range(1, 100, 2):
    S = S + numerator/denominator
    denominator = denominator + 1

print(f"\n\n\t S = {S} \n\n")