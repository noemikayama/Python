# Exemplo usando método f -> Reais

A=10/3
B=333/7
C=1978/11

#########################################################################################

print(f"\n\tSEM FORMATAÇÃO => Valor de A = {A}")
print(f"\n\tSEM FORMATAÇÃO => Valor de B = {B}")
print(f"\n\tSEM FORMATAÇÃO => Valor de C = {C}")
print("\n===============================================================\n")
print(f"\n\t DUAS CASAS DECIMAIS => Valor de A = {A:8.2f}")
print(f"\n\tNENHUMA CASA DECIMAL => Valor de B = {B:8.0f}")
print(f"\n\t UMA CASA DECIMAL => Valor de C = {C:8.1f}")
print("\n===============================================================\n")
# Ler interação com o teclado
input("\t\t\t\t\t\tTecle Algo Para Continuar....")
print("\n===============================================================\n")
print(f"\n\tTAMANHO '8' DUAS CASAS DECIMAIS => Valor de A = {A:8.2f}")
print(f"\n\tTAMANHO '8' DUAS CASAS DECIMAIS => Valor de B = {B:8.2f}")
print(f"\n\tTAMANHO '8' DUAS CASAS DECIMAIS => Valor de C = {C:8.2f}")
print("\n===============================================================\n")
print(f"\n\tTAMANHO '8' DUAS CASAS DECIMAIS COM ZERO => Valor de A = {A:08.2f}")
print(f"\n\tTAMANHO '8' DUAS CASAS DECIMAIS COM ZERO=> Valor de B = {B:08.2f}")
print(f"\n\tTAMANHO '8' DUAS CASAS DECIMAIS COM ZERO=> Valor de C = {C:08.2f}")
print("\n===============================================================\n")
print(f"\n\tTAMANHO '8' UMA CASA DECIMAL ESQUERDA => Valor de B ={B:<8.1f}")
print(f"\n\tTAMANHO '8' UMA CASA DECIMAL CENTRO => Valor de B ={B:^8.1f}")
print(f"\n\tTAMANHO '8' UMA CASA DECIMAL DIREITA => Valor de B ={B:>8.1f}")
print("\n===============================================================\n")

