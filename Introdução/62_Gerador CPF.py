"""
PODEMOS UTILIZAR UM 'IMPORT RANDOM' COM O random.randint() QUE GERA NUMEROS INTEIROS ALEATORIOS

"""
import random

 ### VARIAVEIS  

for _ in range(23): ### COMANDO PARA GERAR 23 CPFs

    cpf_nove_digitos = ''
    multiplicador_digito_01 = 10
    soma_digito_01 = 0

    ### LOOPING PARA GERAR NOVE DIGITOS ALEATORIOS:

    for i in range(9):
        cpf_nove_digitos += str(random.randint(0,9))


    ### LOOPING PARA DESCOBRIR O PRIMEIRO DIGITO:

    for digito in cpf_nove_digitos:
        soma_digito_01 += int(digito) * multiplicador_digito_01
        multiplicador_digito_01 -= 1
    resto_01 = ((soma_digito_01 * 10) % 11)
    digito_01 = resto_01 if resto_01 <= 9 else 0

    ### LOPPING PARA VALIDAR SEGUNDO DIGITO:

    cpf_dez_digitos = cpf_nove_digitos + str(digito_01)
    multiplicador_digito_02 = 11
    soma_digito_02 = 0

    for digito in cpf_dez_digitos:
        soma_digito_02 += int(digito) * multiplicador_digito_02
        multiplicador_digito_02 -= 1
    resto_02 = ((soma_digito_02 * 10) % 11)
    digito_02 = resto_02 if resto_02 <= 9 else 0

    ### VALIDANDO SE OS DIGITOS ESTÃO CORRETOS:

    print(f'{cpf_nove_digitos[0:3]}.'\
          f'{cpf_nove_digitos[3:6]}.'\
          f'{cpf_nove_digitos[6:9]}-{digito_01}{digito_02}')

