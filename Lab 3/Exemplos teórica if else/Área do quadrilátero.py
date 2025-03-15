print("\n\n C Á L C U L O    Á R E A ")
print("\n ====================================")
print("\n\n Entrada de dados: ")

base = float(input("\n Base: "))
altura = float(input("\n Altura: "))

area = base * altura
if (base == altura):
    print(f"\n\n Área do quadrado: {area:.2f}")
else:
    print(f"\n\n Área do retângulo: {area:.2f}")

print("\n\n")