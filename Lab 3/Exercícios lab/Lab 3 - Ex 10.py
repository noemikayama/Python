# Program that read n (given) numbers and add even numbers and counts odd numbers

n = int(input("\n\n Insert how many numbers: "))
i = 0
sum = 0
count = 0

while(i < n):
    num = int(input("\n Insert integer number: "))
    if ((num % 2) == 0):
        sum = sum + num
    else:
        sum = sum
        count = count + 1
    i = i + 1

print(f"\n\n\t Sum = {sum}")
print(f"\n\t Count = {count}")