exit = 1
highest_salary = 0
num_people = 0
sum_salary = 0
sum_children = 0
population = 0

while (exit != 0):
    population = population + 1
    salary = float(input("\n\n Insert your salary: "))
    num_children = int(input("\n Insert number of children: "))
    sum_salary = sum_salary + salary
    sum_children = sum_children + num_children
    if (salary >= highest_salary):
        highest_salary = salary
    if (salary <= 100):
        num_people = num_people + 1
    exit = int(input("\n\n If you want to exit type 0: "))
    
average_salary = sum_salary / population
average_children = sum_children / population
percentual = (num_people / population) * 100

print(f"\n\n\t The population's average salary is R${average_salary} ")
print(f"\n\t The average number of children in the population is {average_children} ")
print(f"\n\t The highest salary is R${highest_salary} ")
print(f"\n\t The percentual of people with salary below R$100 is {percentual:.2f}% \n\n")
