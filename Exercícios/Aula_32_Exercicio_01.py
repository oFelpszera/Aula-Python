"""
Faça um programa que peça ao usuário para digitar um número inteiro,
Informe se este número é PAR ou ÍMPAR. Caso o usuário não digite um número inteiro,
informe que não é um número inteiro.
"""
num_inteiro = input('Digite um Número Inteiro: ')

if num_inteiro.isdigit():

    num_int = int(num_inteiro) # Se eu converto antes do IF, e o usuario digitar numero quebrado, quebra o programa.
    impar_ou_par = num_int % 2 # Criei a variavel para deixar o código legivel, se o resto da divisão "%" for '0' então é 'Par'

    if impar_ou_par == 0:
        print('Seu número é Par. ', end='\n\n')
    else:
        print('Seu número é Impar. ', end='\n\n')
else:
    print('Número digitado não é Inteiro. ', end='\n\n')

