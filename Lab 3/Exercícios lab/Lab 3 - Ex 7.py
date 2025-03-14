# Program that culates raise ording to plan

plan = int(input("\n\n Select the number of your plan (1, 2 or 3): "))
salary = float(input("\n Your current salary: "))

while (plan <= 1 or plan >=3):
    print("\n\n ERROR - INSERT VALID NUMBER\n\n ")
    plan = int(input("\n\n Select the number of your plan (1, 2 or 3): "))
    salary = float(input("\n Your current salary: "))
    
if (plan == 1):
    new_salary = salary + (salary * 0.1) #10% raise
    print(f"\n\nt The new salary is: R${new_salary} \n\n")
if (plan == 2):
    new_salary = salary + (salary * 0.15) #15% raise
    print(f"\n\nt The new salary is: R${new_salary} \n\n")
else:
    new_salary = salary + (salary * 0.2) #20% raise
    print(f"\n\nt The new salary is: R${new_salary} \n\n")