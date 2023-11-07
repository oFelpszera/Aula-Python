# ID = Identidade do objeto
# É o local que o valor da variável se encontra na memoria, sua identificação

variavel_01 = 'A'
variavel_02 = 'A'
variavel_03 = 'b'
variavel_04 = 'B'

# Temos quatro variaveis, duas iguais e duas diferentes, cada uma possui uma ID (Identidade),
# o Python percebe quais são identicas e, utiliza a mesma identidade para buscar 
# esses valores na memória. Se for valores diferentes, ID diferentes

print(id(variavel_01))
print(id(variavel_02)) 
print(id(variavel_03))
print(id(variavel_04))
print('\n')

