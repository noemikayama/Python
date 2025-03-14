# Program that calculates factorial

n = int(input("\n\n Insert a number: "))

i = 1
fact = 1

while (i <= n):
    fact = fact * (n - (n - i))
    i = i + 1
print(f"\n\n\n {n}! = {fact} \n\n")