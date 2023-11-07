# ASPAS INVERTIDA '\' SERVE PARA QUEBRAR A LINHA NO CÓDIGO E CONTINUAR ABAIXO:

frase = 'O Python é uma Linguagem de Programação '\
        'Multiparadigma. '\
        'Python foi criado por Guido Van Rossum.'

print(frase, '\n')

contador = 0
i = 0
letra = input('Qual letra você deseja contar? ').lower()
frase = str(frase.lower())

while i < len(frase):

    if letra == frase[i]:
        contador += 1

    i += 1

print(contador, '\n')


