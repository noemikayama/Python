# Imprimir divisores de um número

num = int(input("\n\n Insira o número a ser analisado: "))
cont = 1

print("\n =============================================== \n")
print(f"\n\n Divisores de {num} ")

for cont in range(1, (num + 1)) :
    if ((num % cont) == 0):
        print(f"\n\t\t {cont}")

print("\n =============================================== \n\n")


