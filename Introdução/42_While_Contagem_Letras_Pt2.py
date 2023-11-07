# CONTAGEM DE LETRAS QUE MAIS APARECEU - DESCONSIDERANDO ESPAÇOS

frase = 'O Python é uma Linguagem de Programação '\
        'Multiparadigma, de tipagem Forte e Dinâmica. '\
        'Python foi criado por Guido Van Rossum.'

print(frase, '\n')

i = 0

letra = ''
qtd_letra = 0

letra_1 = ''
qtd_letra_1 = 0

letra_2 = ''
qtd_letra_2 = 0

while i < len(frase):

    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_letra_atual = frase.count(letra_atual)

    if qtd_letra < qtd_letra_atual:
        qtd_letra = qtd_letra_atual
        letra = letra_atual

    elif qtd_letra_1 < qtd_letra_atual and letra_atual != letra:
        qtd_letra_1 = qtd_letra_atual
        letra_1 = letra_atual 

    elif qtd_letra_2 < qtd_letra_atual and letra_atual != letra and letra_atual != letra_1:
        qtd_letra_2 = qtd_letra_atual
        letra_2 = letra_atual                 

    i += 1

print(
    'A primeira letra que mais apareceu foi '
    f'a letra "{letra}". '
    f'Que apareceu {qtd_letra}x.'
)

print(
    'A segunda letra que mais apareceu foi '
    f'a letra "{letra_1}". '
    f'Que apareceu {qtd_letra_1}x.'
)

print(
    'A terceira letra que mais apareceu foi '
    f'a letra "{letra_2}". '
    f'Que apareceu {qtd_letra_2}x.'
    '\n'
)