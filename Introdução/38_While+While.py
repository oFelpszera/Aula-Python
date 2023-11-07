"""WHILE dentro de outro WHILE
Basicamente ele vai ver uma condição, enquanto ela for verdadeira vai executar, ser tivermos um outro WHILE dentro
dessa primeira condição, enquanto essa segunda for verdadeira, ele vai executar ela, até ser falsa e, continuar no primeiro WHILE"""

qtd_linhas = 3
qtd_colunas = 3

linha = 1
coluna = 'A' # VOU CONCATENAR STRINGS

while linha <= qtd_linhas:

    while coluna == 'A' or coluna == 'B' or coluna == 'C':
        print(f'{linha} {coluna}')
        if coluna == 'A':
            coluna = 'B'
        elif coluna == 'B':
            coluna = 'C'
        else:
            coluna = 'A'
            break

    linha += 1