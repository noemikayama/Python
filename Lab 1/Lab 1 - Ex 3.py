# Program that calculates new salary with the readjustment
salary = float(input("\n Insert salary here (R$): ")) # Get salary
readjustment = float(input("\n Insert readjustment here (%): ")) # Get percentage of the readjustment
new_salary = salary + (salary * (readjustment/100)) # Calculates new salary
print("\n\n\t New salary is: R$", new_salary) # Prints new salary
print("\n\n *END* \n\n")