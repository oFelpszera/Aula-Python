# ENUMERATE É UM COMANDO PARA NUMERAR OS ITENS DE UMA LISTA (COMO SE FOSSE OS ÍNDICES)
# ELE RETORNA EM TUPLAS (LISTA IMUTAVEL)

# SE USARMOS O ENUMERATE E PRINTAR O RESULTADO, ELE VAI APENAS MOSTRAR O LOCAL QUE ESTÁ OCUPANDO NA MEMORIA:
lista = ['Gustavo', 'Amanda', 'Julio', 'Bianca']
lista_enumerada = enumerate(lista)
print(lista_enumerada) # <enumerate object at 0x000001AEF1487510>
print('\n')

# PODEMOS UTILIZAR O 'FOR/IN' PARA TRAZER OS RESULTADOS ENUMERADOS
for item in lista_enumerada:
    print(item)
print('\n')

# ESSE FOR/IN SÓ FUNCIONA UMA UNICA VEZ, É COMO SE DEPOIS DE PERCORRER TODOS OS ITENS E ENUMERAR
# ELE APAGASSE AS INFORMAÇÕES, NÃO SENDO POSSÍVEL EXECUTAR UM NOVO 'FOR/IN'
for item in lista_enumerada:
    print(item) # Sem resultado

# UMA MANEIRA DE SOLUCIONAR ISSO, É CHAMAR O 'ENUMERATE' DIRETO NO 'FOR/IN':
for item in enumerate(lista):
    print(item)
for item in enumerate(lista):
    print(item)
print('\n')

# OUTRA DETALHE É QUE PODEMOS FAZER O DESEMPACOTAMENTO DIRETO NO FOR:
for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)
print('\n')

# PARA EVITAR CRIAR UMA LINHA DESEMPACOTANDO, PODEMOS FAZER ISSO DIRETO NO 'FOR/IN':
for indice, nome in enumerate(lista):
    print('\t', indice, nome) # '\t' é um TAB
print('\n')

  