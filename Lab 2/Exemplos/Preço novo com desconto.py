old_price = float(input("\n Insert old price (R$): "))
discount = float(input("\n Insert dicount (%): "))
new_price = old_price - (discount*old_price)/100
print(f"\n\n\t Old price: R$ {old_price:.2f}")
print(f"\n\t Discount: {discount:.2f} %")
print(f"\n\t New price: R$ {new_price:.2f}")
print("\n\n\t\t *END* \n\n")

