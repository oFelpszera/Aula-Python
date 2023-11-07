"""
TIPOS INT E FLOAT
int -> Números Inteiros (1 - 2 - 3...) // float -> Números Flutuantes (1.1 - 1.2 - 1.3...)
Não interfere se for positivo ou negativo. Número float são sempre separados por "ponto"
"""
print(23) # int (positivo)
print(-23) # int (negativo)
print(23.32) # float (positivo)
print(-23.32) # float (negativo)
"""
Eu posso solicitar o comando "print" com outro comando dentro, para ele me dizer 
qual o tipo "type", da função. // type é uma classe (class), print é uma função (function)
"""
print(23, type(23)) # Vai me retornar como 'int', pois é um número inteiro
print(23.32, type(23.32)) # Vai me retornar como 'float', pois é um número flutuante
print('Felps', type('Felps')) # Vai me retornar como 'str', pois é uma string, texto.