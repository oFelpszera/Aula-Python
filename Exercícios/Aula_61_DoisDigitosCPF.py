cpf = input('Digite os NOVE primeiros digitos do seu CPF: ')
multiplicador = 10
indicador = 0
soma_digito_01 = []
soma_digito_02 = []

if len(cpf) == 9:

    for digito in cpf:
       
        digito_inteiro = int(digito)
        multiplicacao = digito_inteiro * multiplicador
        soma_digito_01.append(multiplicacao)
        multiplicador -= 1
        indicador += 1
    
    multiplicador = 11
    indicador = 0
    resto_01 = (sum(soma_digito_01) * 10) % 11
    digito_01 = resto_01 if resto_01 <= 9 else 0

    cpf = cpf + str(digito_01)

    for digito in cpf:
        digito_inteiro = int(digito)
        multiplicacao = digito_inteiro * multiplicador
        soma_digito_02.append(multiplicacao)
        multiplicador -= 1
        indicador += 1

    resto_02 = (sum(soma_digito_02) * 10) % 11
    digito_02 = resto_02 if resto_02 <= 9 else 0

    print(f'Os últimos números do seu CPF é {digito_01}{digito_02}.\n '
          f'O número completo é {cpf}{digito_02} \n')

else:
    print('Quantidade de caractéres inválidos! \n')