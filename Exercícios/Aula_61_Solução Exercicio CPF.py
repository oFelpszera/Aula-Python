cpf = input('Olá, digite os números do seu CPF: ')
digitos_cpf = cpf[:9]
multiplicador_digito_01 = 10
soma_digito_01 = 0

### VALIDANDO PRIMEIRO DIGITO:

if len(cpf) == 11:

    for digito in digitos_cpf:
        soma_digito_01 += int(digito) * multiplicador_digito_01
        multiplicador_digito_01 -= 1
    resto_01 = ((soma_digito_01 * 10) % 11)
    digito_01 = resto_01 if resto_01 <= 9 else 0

### VALIDANDO SEGUNDO DIGITO:

    digitos_cpf = cpf[:9] + str(digito_01)
    multiplicador_digito_02 = 11
    soma_digito_02 = 0

    for digito in digitos_cpf:
        soma_digito_02 += int(digito) * multiplicador_digito_02
        multiplicador_digito_02 -= 1
    resto_02 = ((soma_digito_02 * 10) % 11)
    digito_02 = resto_02 if resto_02 <= 9 else 0

### VALIDANDO SE OS DIGITOS ESTÃO CORRETOS:

    if digito_01 == int(cpf[9]) and digito_02 == int(cpf[10]):
        print('CPF Válido! \n')
    else:
        print('CPF Inválido! \n')

else:
    print('Existem caractéres inválidos! \n')

    