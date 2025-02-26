# Programs that simulates a cashier operation 
purchase = float(input("\n Insert purchase amount (R$): ")) # Gets total purchase amount
amount = float(input("\n Amount paid by the customer (R$): ")) # Gets total paid by the customer
change = amount - purchase # Calculates change
print("\n Total change (R$): ", change) # Prints total change
bill_100 = change // 100 # Amount of R$100
bill_50 = (change - 100*bill_100) // 50 # Amount of R$50
bill_20 = (change - 100*bill_100 - 50*bill_50) // 20 # Amount of R$20
bill_10 = (change - 100*bill_100 - 50*bill_50 - 20*bill_20) // 10 # Amount of R$10
bill_5 = (change - 100*bill_100 - 50*bill_50 - 20*bill_20 - 10*bill_10) // 5 # Amount of R$5
bill_1 = (change - 100*bill_100 - 50*bill_50 - 20*bill_20 - 10*bill_10 - 5*bill_5) # Amount of R$1
print("\n\n\t BILLS: ") 
print("\n\t\t R$100: ", bill_100) # Prints the amount of R$100 bills
print("\n\t\t R$50: ", bill_50) # Prints the amount of R$50 bills
print("\n\t\t R$20: ", bill_20) # Prints the amount of R$20 bills
print("\n\t\t R$10: ", bill_10) # Prints the amount of R$10 bills
print("\n\t\t R$5: ", bill_5) # Prints the amount of R$5 bills
print("\n\t\t R$1: ", bill_1) # Prints the amount of R$1 bills
print("\n\n *END* \n\n")