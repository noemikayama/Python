
print("\n\n Degrees Fahrenheit \t | \t\t Degrees Celsius ")
print("\n ____________________ \t | \t ___________________________________ \n")

for fahrenheit in range(30, 51, 2):
    celsius = ((fahrenheit - 32))/(9/5)
    print(f"\t {fahrenheit}ºF \t\t | \t\t {celsius}ºC")