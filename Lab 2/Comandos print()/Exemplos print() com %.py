# Exemplos utilizando o formato %

idade = 16

#####################################################

# Formas diferentes de imprimir

# Sem formatação definida
print("\n Sem formatação -> idade %d \n" %idade)
# Especificando 5 casas/espaços, alinhado/identado a partir da direita
print(" Especificando 5 espaços, idento a partir da direita -> idade %5d \n" %idade)
# 5 espaços com zeros nos espaços vazios, alinhado/identado a partir da direita
print(" 5 espaços, com zeros, idento a partir da direita -> idade %05d \n" %idade)
# 5 espaços, alinhado/identado a partir da esquerda
print(" 5 espaços, idento a partir da equerda -> idade %-5d \n" %idade)

