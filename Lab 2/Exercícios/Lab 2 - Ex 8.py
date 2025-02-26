# Program that switchets digits

num = int(input("\n Insert 3 digit number: ")) #Gets a 3 digit number
dig_1 = num//100 #Calculates first digit
dig_2 = (num - (dig_1*100))//10 #Calculates second digit
dig_3 = num - (dig_1*100) - (dig_2*10) #Calculates third digit
print("\n\n\t The number was: ", num) #Prints inserted number
print(f"\n\n\t Now the number is {dig_3}{dig_2}{dig_1}") #Prints new number
print("\n\n\t\t *END* \n\n") 
