# Program that converts dolars to reais

exchange_rate = 5.74 # US$1.00 = R$5.74
dolars = float(input("\n Insert amount in dolars (US$): ")) # Gets the amount in dolars
reais = dolars*exchange_rate # Conversion
print(f"\n\n\t US$ {dolars:.2f} is R$ {reais:.2f}") # Prints amounts in dolars and reais
print("\n\n\t\t *END* \n\n")