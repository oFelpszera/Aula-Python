# FOR CAMINHA POR TODOS OS INDICES DA VARIAVEL, ONDE PODEMOS DEFINIR ALGUMA COISA.
# COMO NA LISTA, CADA ITEM POSSUI UM INDICE, TAMBÉM PODEMOS ACESSA-LOS ATRAVÉS DO FOR

lista = [
    'Felipe', 'Giovanna', 'Felipe', 'Haroldo', 'Felipe', 'Giovanna', 'Sueli'
]

for nome in set(lista): 
    print(f'O nome {nome}, apareceu {lista.count(nome)}x')
    
# O 'SET()' GUARDA OS VALORES DA LISTA EXCLUINDO O QUE É REPETIDO



