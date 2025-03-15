# Programs that read 5 numbers and gives the sum and the average

i = 1
sum = 0

while (i <= 5):
    num1 = int(input("\n\n Insert number: "))
    sum = sum + num1
    i = i + 1

average = sum / 5

print(f"\n\n\t Sum = {sum}")
print(f"\n\t Average = {average} \n\n")

