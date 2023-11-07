# CONTINUE é uma maneira de informar que o códgigo deve continuar no WHILE desconsiderando
# a condição que contém o CONTINUE

contador = 0

while contador <= 100:
    contador += 1

    if contador == 23:
        print(f'Não vou mostrar o número {contador}')
        continue

    if contador >= 30 and contador <= 40:
        print(f'Não vou mostrar o número {contador}')
        continue

    print(contador) # IMPORTANTE COLOCAR O PRINT DEPOIS DA CONDIÇÃO, SE NÃO ELE IMPRIME O NÚMERO QUE QUEREMOS PULAR
    
    if contador == 50:
        break


