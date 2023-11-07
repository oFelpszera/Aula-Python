# WHILE / ELSE

# POUCO UTILIZADO, ELE RETORNA UM VALOR DEPOIS QUE O LOOP DO WHILE É FINALIZADO!
# É COMO SE FOSSE UM CÓDIGO FORA DO WHILE, A DIFERENÇA É QUE O ELSE PODE OU NÃO, SER EXECUTADO, 
# SE TIVER UM 'BREAK' NÃO SERÁ.

# EX.: COM ELSE DENTRO DO WHILE E CÓDIGO FORA DO WHILE:

valor = 'Felipe Andrade'
i = 0 # VARIAVEL 'i' = INDICE

while i < len(valor):
    print(valor[i])
    i += 1

else:
    print('Else dentro do While.')

print('Código fora do While.' '\n')

# EX.: UTILIZANDO BREAK O ELSE NÃO SERÁ EXECUTADO:

valor = 'Felipe Andrade'
i = 0 

while i < len(valor):
    letra = valor[i]
    
    if letra == ' ':
        break

    print(letra)
    i += 1
    
else:
    print('Else dentro do While.') # NÃO É EXECUTADO, POIS AO ENCONTRAR UM ESPAÇO O CÓDIGO É ENCERRADO 'BREAK'

print('Código fora do While.')