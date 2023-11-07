contador = 0

while contador < 10:
    contador = contador + 1
    print(contador)

print('Acabou a contagem')

""" No exemplo acima, temos o contador '0', quando entrar no WHILE ele vai ver se '0' é menor que '10'
no caso será verdadeiro, então ele vai gerar uma nova variavel CONTADOR que será o contador '0' + '1'
nesse momento o contador antigo '0' passárá a ser '1' que entrará no WHILE e verificará se é menor que '10' e,
repetir o processo. """

""" Ele só imprime o número '10', pois ele entra no WHILE sendo '9' que é menor que '10',
depois que entrou que ele soma mais '1' """

""" A Ordem da soma e do print, influencia, pois se imprimirmos antes de somar, ele vai imprimir
o número anterior, se apenas fizermos a alteração, ao invés de '1' a '10' será de '0' a '9' """

contador = 0

while contador < 10:
    print(contador)
    contador = contador + 1

print('Acabou a contagem')