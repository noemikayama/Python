# Program that calculates salary of a plumber after taxes given the amount of days

salary_per_day = 30 #Amount paid by day
days = int(input("\n Insert number of days: ")) #Gets number of days
after_taxes = (salary_per_day*days)*0.92 #Calculates salary after 8% of taxes
print(f"\n\n\t Final salary based on {days} days is R${after_taxes:.2f}") #Prints final salary