num = int(input("\n\n Insert number: "))
even = 0
odd = 0
sum_even = 0
sum_all = 0

while (num != 0):
    if ((num % 2) == 0):
        even = even + 1
        sum_even = sum_even + num
        sum_all = sum_all + num
    else:
        odd = odd + 1
        sum_all = sum_all + num
    num = int(input("\n\n Insert number: "))

average_even = sum_even / (odd + even)
average_all = sum_all / (odd + even)

print("\n\n\t There were: ")
print(f"\n\t - {odd} odd numbers")
print(f"\n\t - {even} even numbers")
print("\n\n\t The averages are:")
print(f"\n\t - {average_even:.2f} it's the average of all the even numbers")
print(f"\n\t - {average_all:.2f} it's the average of all the numbers \n\n")