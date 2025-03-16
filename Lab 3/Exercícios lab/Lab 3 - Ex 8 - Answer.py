base = int(input("\n\n Base: "))
exp = int(input("\n Exponent: "))

power = 1
count = 1

while (count <= exp):
    power = power * base
    count = count + 1

print(f"\n\n\t {base}^{exp} = {power} \n\n")


