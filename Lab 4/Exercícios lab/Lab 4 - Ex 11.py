elder = 0
sum_height = 0
below50_wheight = 0

for i in range(1, 26):
    age = int(input("\n\n Insert your age: "))
    height = float(input("\n Insert your height in meters: "))
    wheight = float(input("\n Insert your wheight in kilos: "))
    if (age > 50):
        elder = elder + 1
    if (age > 10 and age < 20):
        sum_height = sum_height + height
    if (wheight < 50):
        below50_wheight = below50_wheight + 1

average_height = sum_height / 25
percentual = (below50_wheight / 25) * 100

print(f"\n\n\t - The amount of people with age above 50 is: {elder}")
print(f"\n\t - The average height of people with ages between 10 and 20 is: {average_height:.2f}m")
print(f"\n\t - The percentual of people with wheight below 50kg is: {percentual} \n\n")