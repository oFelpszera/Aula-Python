# INTERPOLAÇÃO BÁSICA DE STRINGS 
# É você "interpolar" um dado, sem precisar digita-lo, basta utilizar % e a "Letra Referência"
"""
s       -    strings      -    "str"
d ou i  -    inteiro      -    "int"
f       -    flutuante    -    "float"
x ou X  -    hexadecimal  -    "ABCDEF0123456789"

"""

nome = 'Felipe Andrade'
preco = 100000.9965332

variavel_00 = (f'{nome}, o preço é, {preco}') 
# SEM INTERPOLAÇÃO
variavel_01 = 'Felipe, o preço é R$%f' % preco
# UMA ÚNICA INTERPOLAÇÃO NÃO PRECISA DE PARENTESES NA VARIAVEL
variavel_02 = '%s, o preço é R$%f' % (nome, preco) 
# COM INTERPOLAÇÃO %s "str" e, %f "float" - DUAS INTERPOLAÇÃO PRECISA DE PARENTESES NA VARIAVEL
variavel_03 = '%s, o preço é R$%.3f' % (nome, preco)
# COM INTERPOLAÇÃO E FORMATAÇÃO DE CASAS DECIMAIS

print(variavel_00, variavel_01, variavel_02, variavel_03, sep='\n', end='\n\n')
print('O Hexadecimal de %d é %03x' %(1500, 15)) # 3 CASAS DECIMAIS
# "x" MINUSCULO, HEXADECIMAL MINUSCULO
print('O Hexadecimal de %d é %03X' %(1500, 15), end='\n\n') 
# "X" MAIUSCULO, HEXADECIMAL MAIUSCULO

