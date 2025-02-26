base_salary = 1500
num_cars = int(input("\n Insert number of sold cars: "))
total_sales = float(input("\n Insert car sales (R$): "))
comission = 0.05*total_sales
aditionals = num_cars*200 + comission
salary = base_salary + aditionals
print(f"\n\n\t - Base Salary: R$ {base_salary:<8.2f}")
print(f"\n\t - Number of sold cars: {num_cars:<8.0f}")
print(f"\n\t - Total sales: R$ {total_sales:<8.2f}")
print(f"\n\t - Comission: R$ {comission:<8.2f}")
print(f"\n\t - Total of aditionals: R$ {aditionals:<8.2f}")
print(f"\n\t - Final salary: R$ {salary:<8.2f}")
print("\n\n\t\t *END* \n\n")
