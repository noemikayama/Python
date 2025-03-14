# Program that get 2 grades (T1 and T2) and the wheights (W1 and W2) and calculates weighted average

T1 = float(input("\n\n Insert grade of the first test: "))
T2 = float(input("\n Insert grade of the second test: "))
W1 = int(input("\n\n Insert wheight of the first test (in %): "))
W2 = float(input("\n Insert wheight of the second test (in %): "))

while (T1 >= 0 and T2 >= 0 and W1 > 0 and W2 > 0):
    average = ((T1 * W1) + (T2 * W2))/100       # Calculates the wheighted average
    if (average >= 5 and average < 10):
        print(f"\n\n\t Approved with an average of: {average:.1f}\n\n")
    elif (average == 10):
        print(f"\n\n\t Approved with excelency with an average of: {average:.1f} \n\n")
    else:
        print(f"\n\n\t Failed with an average of: {average:.1f} \n\n")
    T1 = float(input("\n\n Insert grade of the first test: "))
    T2 = float(input("\n Insert grade of the second test: "))
    W1 = int(input("\n\n Insert wheight of the first test (in %): "))
    W2 = float(input("\n Insert wheight of the second test (in %): "))