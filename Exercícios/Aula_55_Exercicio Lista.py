"""
CRIAR UMA LISTA DE COMPRAS COM LISTA
O USUARIO DEVE TER A POSSIBILIDADE DE:
INSERIR, APAGAR, LISTAR OS VALORES DA LISTA
NÃO PERMITA QUE O PROGRAMA QUEBRE COM ERROS DE ÍNDICES.

"""
from termcolor import colored
import os

lista = []
print(colored('BEM-VINDO À SUA LISTA DE COMPRAS! \n', 'blue'))

while True:
    
    print(colored('\nO QUE VOCÊ DESEJA FAZER?', 'yellow'))
    print('\n\t[I] Inserir   [A] Apagar   [V] Visualizar   [S] Sair')        
    shopping = input(colored('\n\tDigite Aqui: ', 'yellow')).upper()

    ### VISUALIZAR LISTA NUMERADA:
               
    if shopping == 'V' and len(lista) >= 1:
        os.system('cls')
        print(colored('\nLISTA DE COMPRAS:', 'blue'))
        for indice, nome in enumerate(lista):            
            print(colored(f'\t {indice} {nome}', 'yellow'))
        
    elif shopping == 'V' and len(lista) == 0:
        print(colored('\tNão há itens para visualizar! \n', 'red'))    

    ### INSERIR ITEM NA LISTA:

    elif shopping == 'I':
        os.system('cls')
        item = input(colored('Digite o nome do Item: ', 'yellow')).capitalize()
        lista.append(item)
        print(colored('Item Adicionado! \n', 'yellow'))

    ### APAGAR ITEM DA LISTA:   
                             
    elif shopping == 'A' and len(lista) >= 1:
        os.system('cls')

        try:
            delete = int(input(colored('Qual o número do item que deseja apagar? ', 'yellow')))
            del lista[delete]
            print(colored('Item Deletado! \n', 'yellow'))

        except ValueError:
            print(colored('Digite apenas Número! \n', 'red'))

        except IndexError:
            print(colored('Número do item não existe! \n', 'red'))


    elif shopping == 'A' and len(lista) == 0:
        print(colored('\tNão há itens para apagar \n', 'red'))

    ### SAIR
    elif shopping == 'S':
        os.system('cls')
        print('Boas Compras! \n')
        break

    else: 
        print(colored('\tLetra Inválida! \n', 'red'))

