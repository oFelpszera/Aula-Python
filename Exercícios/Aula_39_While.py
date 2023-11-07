# FAZER ALGUMA MODIFICAÇÃO COM VARIA ITERAVEL (POSSUI INDICES) COM WHILE:

nome = 'Felipe Andrade'
qtd_caracteres = len(nome)
print(f'Seu nome é: {nome} e, tem {qtd_caracteres} caracteres.', '\n')

indice = 0
nome02 = ''

"""while indice < len(nome):

    if indice == 6:
        indice += 1
        continue
   
    print(f'{nome[indice]:*^3}')
    indice += 1"""

### O DE CIMA FUNCIONOU, MAS NA VERTICAL, ABAIXO É A VERSÃO PARA RESULTAR TUDO NA HORIZONTAL

while indice < len(nome):

    letra = nome[indice]
    nome02 += f'*{letra}'

    indice += 1
print(f'{nome02}')


