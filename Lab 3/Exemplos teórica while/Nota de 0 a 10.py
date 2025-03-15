# Program that gets a grade and informs if it's valid or not

grade = float(input("\n\n Insert grade here: "))

while (grade <= 0 or grade >= 10):
    print("\n\n Invalid grade \n\n")
    grade = float(input("\n\n Insert grade here: "))
else:
    print("\n\n Valid grade \n\n")

