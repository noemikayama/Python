# Uso do comando while com else: imprima o valor do número digitado até 5

# Variável de controle
a = int(input("\n\n Digite um número inteiro: "))

while (a <= 5) :            # Condição de parada
    print(a)
    a = a + 1           # Incremento
else :          # "Senão" (se a > 5)
    print(f"\n\n {a} > 5 \n\n")

print("\n\n\t Fim do programa \n\n")

