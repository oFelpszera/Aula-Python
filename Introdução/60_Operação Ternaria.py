"""
OPERAÇÃO TERNÁRIA É UM IF/ELSE EM UMA ÚNICA LINHA
RETORNA UM VALOR SE A CONDIÇÃO FOR VERDADEIRA OU OUTRO SE FOR FALSA

"""

### EXEMPLO 01:

condicao = 10 == 10
nova_condicao = 'Verdade' if condicao else 'Falso'
# O valor da variável 'nova_condicao' retornará 'Verdade' se o if baseado na variável 'condicao' for verdade
# Como sabemos que 10 é igual a 10, então o print retornará 'Verdade':
print(nova_condicao)

# Caso a condição fosse 10 == 11, o print retornaria 'Falso'.



### EXEMPLO 02:
# Poderiamos fazer o IF direto no 'print':

print('Verdade' if True else 'Falso') # IF TRUE (Se Verdade), imprime o valor 'Verdade'
print('Verdade' if False else 'Falso') # IF FALSE (Se Falso), imprime o valor 'Falso' do ELSE.



### EXEMPLO 03:
# Condição de Maior ou Igual:

digito = 6
novo_digito = digito if digito <= 9 else 0 
# Imprime o valor do 'digito' SE o 'digito' for menor ou igual a 9, SENÃO imprime 0
print(novo_digito)

# Se alterar o valor do digito para 10 (contendo dois dígitos) o valor retornado será 0. 



### EXEMPLO 04:
# Mais de um IF na condição:

print('Valor 01' if False else 'Valor 02' if False else 'Valor 03' if True else 'Valor 04')
# Se o primeiro IF for verdade, vai imprimir 'Valor 01'
# Se não for, o 'Valor 02' só irá aparecer SE o segundo IF ser verdade e assim sucessivamente.





