# CRIAR UMA LISTA E, IMPRIMIR OS ITENS COM O NÚMERO DO ÍNDICE:

lista = [
    'Felipe', 'Giovanna', 'Felipe', 'Haroldo', 'Felipe', 'Giovanna', 'Sueli'
]

indice = 0

lista.append('Luiz')

for nome in lista: 
    print(indice, nome)
    indice += 1


# NA SOLUÇÃO DO EXERCICIO ELE UTILIZOU UM 'RANGE' CONSIDERANDO O 'LEN' DA LISTA:

lista = [
    'Felipe', 'Giovanna', 'Felipe', 'Haroldo', 'Felipe', 'Giovanna', 'Sueli'
]

lista.append('Valeria')

indices = range(len(lista)) # len(lista) retornará 7 (itens), logo meu range irá ter o STOP em '7'

for i in indices:
    print(i, lista[i])

    # IMPRIME O 'i' QUE É O NÚMERO + O ÍNDICE DESSE NÚMERO DENTRO DA LISTA EX.:

    # i = '0' 
    # lista[0] = 'Felipe'

    # i = '1'
    # lista[1] = 'Giovanna'

    # [...]

