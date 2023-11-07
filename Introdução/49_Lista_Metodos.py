# É POSSÍVEL CRIAR, LER, ATUALIZAR E APAGAR DADOS DA LISTA
# CHAMAMOS ISSO DE CRUD QUE SÃO AS INICIAIS PARA:
# CREATE - READ - UPDATE - DELETE

# EXISTEM ALGUNS METODOS QUE PODEMOS UTILIZAR NA LISTA:

# APPEND -> Adiciona um item ao final da lista
# POP -> Remove o último item da lista ou, do índice informado 
# DEL -> Deleta um item da lista de acordo com o índice informado
# INSERT -> Insere um item de acordo com o índice informado utilizando dois argumentos (INDICE, ITEM)
# EXTEND -> Estende a lista 
# CLEAR -> Limpa a lista
# (+) -> Concatena uma lista

lista = [10, 20, 30, 40, 50]

# APPEND -> Adiciona um item ao final da lista:
lista.append(60)
print(lista) ##### 10, 20, 30, 40, 50, 60 

# POP -> Remove o último item da lista ou, do índice informado 
lista.pop()
print(lista) ##### 10, 20, 30, 40, 50

# PODEMOS USAR O POP PARA INFORMAR O ÍNDICE QUE QUEREMOS APAGAR
# POR EXEMPLO O INDICE '2' QUE REPRESENTA O NÚMERO 30:
lista.pop(2)
print(lista) ##### 10, 20, 40, 50

# O IDEAL É SEMPRE ADICIONAR OU EXCLUIR INTENS DO INICIO OU DO FINAL, POIS O PYTHON REORGANIZA
# TODA A LISTA, ENTÃO SE TIRARMOS UM ITEM DO MEIO, OS INDICES SERÃO ALTERADOS, SE FOR UMA LISTA
# COM MILHARES DE ITENS, EXIGIRÁ UM PROCESSADOR BOM PARA QUE A REALOCAÇÃO DE INDICE SEJAM FEITAS.

# DEL -> Deleta um item da lista de acordo com o índice informado
del lista[-1] # Estou informando o último item da lista '-1'
print(lista) ##### 10, 20, 40

# INSERT -> Insere um item de acordo com o índice informado utilizando dois argumentos (INDICE, ITEM)
lista.insert(2, 30)
print(lista) ##### 10, 20, 30, 40 

# (+) -> Concatena uma lista 
lista_01 = [1, 2, 3]
lista_02 = [3, 4, 5]
lista_03 = lista_01 + lista_02
print(lista_03) ### 1, 2, 3, 3, 4, 5

# EXTEND -> Estende a lista direto na variável
lista_04 = lista_01.extend(lista_02)
print(lista_04) ### NONE - Não Valor

# GERALMENTE QUANDO NONE APARECE, É POR QUE O PYTHON EXECUTOU A AÇÃO, MAS NÃO NA VARIÁVEL QUE PEDIMOS
# E SIM, NA PROPRIA VARIAVEL QUE RECEBEU A AÇÃO, NO NOSSO CASO, A 'LISTA_01' QUE RECEBEU O 'EXTEND'

print(lista_01)

# CLEAR -> Limpa a lista
lista.clear()
lista_01.clear()
lista_02.clear()
lista_03.clear()
print(lista, lista_01, lista_02, lista_03)
