# Imprimir divisores de um número

num = int(input("\n\n Insira o número a ser analisado: "))
cont = 1

print("\n =============================================== \n")
print(f"\n\n Divisores de {num} ")

while (cont <= num):
    if ((num % cont) == 0):
        print(f"\n\t\t {cont}")
    cont = cont + 1

print("\n =============================================== \n\n")


