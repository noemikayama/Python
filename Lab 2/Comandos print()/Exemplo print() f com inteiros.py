# Exemplo usando o método f -> Inteiros

A=3
B=17
C=135

#########################################################################################

print(f"\n\tSEM FORMATAÇÃO => Valor de A = {A}")
print(f"\n\tSEM FORMATAÇÃO => Valor de B = {B}")
print(f"\n\tSEM FORMATAÇÃO => Valor de C = {C}")
print("\n===============================================================\n")
print(f"\n\tTAMANHO '5' => Valor de A = {A:5d}")
print(f"\n\tTAMANHO '5' => Valor de B = {B:5d}")
print(f"\n\tTAMANHO '5' => Valor de C = {C:5d}")
print("\n===============================================================\n")
# Ler interação com o teclado
input("\t\t\t\t\t\tTecle Algo Para Continuar....")
print("\n===============================================================\n")
print(f"\n\tTAMANHO '5' COM ZERO => Valor de A = {A:05d}")
print(f"\n\tTAMANHO '5' COM ZERO => Valor de B = {B:05d}")
print(f"\n\tTAMANHO '5' COM ZERO => Valor de C = {C:05d}")
print("\n===============================================================\n")
print(f"\n\tTAMANHO '5' ESQUERDA => Valor de B ={B:<5d}")
print(f"\n\tTAMANHO '5' CENTRO => Valor de B ={B:^5d}")
print(f"\n\tTAMANHO '5' DIREITA => Valor de B ={B:>5d}")
print("\n===============================================================\n")
print(f"\n\tTAMANHO '5' COM ZERO ESQUERDA => Valor de B ={B:<05d}")
print(f"\n\tTAMANHO '5' COM ZERO CENTRO => Valor de B ={B:^05d}")
print(f"\n\tTAMANHO '5' COM ZERO DIREITA => Valor de B ={B:>05d}")
print("\n===============================================================\n")

