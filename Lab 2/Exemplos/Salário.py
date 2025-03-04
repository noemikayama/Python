salary = float(input("\n Insert salary: R$ "))
adj = float(input("\n Insert adjustment (%): "))
new_salary = salary + adj*salary/100
print(f"\n\n\t The salary was R${salary:.2f}, with an adjustment of {adj:.1f}%, is now R${new_salary:.2f}")
print("\n\n\t\t *END* \n\n")


