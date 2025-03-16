# Programa que pega n números inseridos, soma os pares e conta os ímpares

n = int(input("\n\n Digite a quantidade de números a ser lida: "))
contImpar = 0
somaPar = 0
cont = 0

while (cont < n):
    num = int(input("\n\n Digite um número: "))
    if ((num % 2) == 0):
        somaPar = somaPar + num
    else:
        contImpar = contImpar + 1
    cont = cont + 1

print(f"\n\n\t A soma de pares lidos é {somaPar}")
print(f"\n\t Foram lidos {contImpar} números ímpares \n\n")

