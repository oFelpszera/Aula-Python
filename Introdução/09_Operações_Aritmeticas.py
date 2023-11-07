# OPERAÇÕES ARITMÉTICAS

adicao = 12 + 11
print('Soma:', adicao, end='.\n')
# Resultado 23 - Type: "int"

subtracao = 55 - 32
print('Subtração:', subtracao, end='.\n')
# Resultado 23 - Type: "int"

multiplicacao = 10 * 10
print('Multiplicação:', multiplicacao, end='.\n')
# Resultado 100 - Type: "int"

divisao = 50 / 4
print('Divisão:', divisao, end='.\n')
# Retorna um número quebrado - Type: sempre será "float"

divisao_inteira = 50 // 4
print('Divisão Inteira:', divisao_inteira, end='.\n') 
# Retorna um número sem casa decimais - Type: "int" ou "float"

exponencial = 2 ** 10
print('Exponencial:', exponencial, end='.\n')
# Retorna o resultado de 2 elevado a 20 - Type: "int" ou "float"

modulo = 55 % 5 
print('Módulo:', modulo, end='.\n\n')  
# Retorna o resto da divisão entre os números

""" O módulo serve para saber se um número é inteiro (divisivel por outro)
ou, podemos dividir por dois, para saber se é par """

modulo_01 = 100 % 10 # Retorna "0" - Type: "int"
print('Resto da Divisão:', modulo_01, end='.\n')

modulo_02 = 100 % 3 # Retorna o "resto" - Type: "int"
print('Resto da Divisão:', modulo_02, end='.\n')

modulo_03 = 40 % 2 # Coloquei "==" 0, se "True" então 40 é par - Type: "bool"
print('Número 40 é Par:', modulo_03 == 0, end='.\n')

modulo_04 = 55 % 2 # Coloquei "==" 0, se "False" então 55 é impar - Type: "bool"
print('Número 55 é Par:', modulo_04 == 0, end='.\n\n')

