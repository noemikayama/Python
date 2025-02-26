# Exemplos usando o método .format

nome = "Ana Beatriz"
idade = 30
peso = 49.56345

#####################################################################################

# Sem espaços específicos e sem identação
print("\n\n Nome: {} \t Idade: {}anos \t\t Peso:{}kg\n" .format(nome, idade, peso)) 

# 15 espaços para nome; 3 espaços para idade; duas casas decimais para peso

# Sem alinhamento/identação
print(" Nome: {:15} \t Idade: {:3}anos \t Peso:{:.2f}kg\n" .format(nome, idade, peso)) 
# Alinhado/identado para a esquerda
print(" Nome: {:<15} \t Idade: {:<3}anos \t Peso:{:.2f}kg\n" .format(nome, idade, peso)) 
# Alinhado/identado para a direita
print(" Nome: {:>15} \t Idade: {:>3}anos \t Peso:{:.2f}kg\n" .format(nome, idade, peso)) 
# Alinhado/identado no centro
print(" Nome: {:^15} \t Idade: {:^3}anos \t Peso:{:.2f}kg\n" .format(nome, idade, peso))

