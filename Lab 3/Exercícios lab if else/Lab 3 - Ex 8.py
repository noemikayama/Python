# Program that calculates xˆn without **

x = int(input("\n\n Insert base: "))
n = int(input("\n\n Insert exponent: "))
aux = n

result = 1

while (n >= 1):
    result = x * result
    n = n - 1 

print(f"\n\n\t {x}^{aux} = {result}")