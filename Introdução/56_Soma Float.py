"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html

"""

# ESSA IMPRECISÃO OCORRE DEVIDO A MANEIRA QUE O NUMERO FLOAT É SALVO NA MEMORIA

float_01 = 0.1
float_02 = 0.7
float_03 = float_01 + float_02

# AO INVÉS DE 0.8 QUE SERIA O RESULTADO DA SOMA, ELE RESULTA '0.799...'
print(float_03) # 0.7999999999999999
print(type(float_03)) # <class 'float'>


# UMA MANEIRA DE CORRIGIR ISSO É UTILIZANDO FSTRINGS (FORMAT):
print(f'{float_03:.2f}') # 0.80
print(type(f'{float_03:.2f}')) # <class 'str'>


# OUTRA MANEIRA SERIA USANDO O ROUND COM A QUANTIDADE DE CASAS DECIMAIS:
# Não aparece o zero no final, pois o ROUND apenas arredonda. 
print(round(float_03, 2)) # 0.8
print(type(round(float_03, 2))) # <class 'float'>


# OUTRA MANEIRA SERIA IMPORTANDO UM MODULO CHAMADO DECIMAL (decimal):
import decimal

float_01 = decimal.Decimal('0.1') # O NÚMERO PRECISA ESTAR EM STRING PARA O DECIMAL CONVERTER CORRETAMENTE
float_02 = decimal.Decimal('0.7')
float_03 = float_01 + float_02

print(float_03) # 0.8
print(type(float_03)) # <class 'decimal.Decimal'>  


# ESSE MODULO DECIMAL SERVE PARA QUANDO QUEREMOS CALCULAR UM NÚMERO COM MAIOR PRECISÃO, POIS ELE VERIFICA
# ATÉ O ULTIMO NÚMERO '0000001' 

# SE IMPRIMIRMOS O RESULTADO DA SOMA SEM CONVERTER OS VALORES PARA STRING A SOMA SERÁ MAIS DETALHADA:
float_01 = decimal.Decimal(0.1) 
float_02 = decimal.Decimal(0.7)
float_03 = float_01 + float_02

print(float_03) # 0.7999999999999999611421941381 -> TEM MUITO MAIS NÚMEROS DO QUE O PRIMEIRO PRINT ACIMA
print(type(float_03)) # <class 'decimal.Decimal'>  