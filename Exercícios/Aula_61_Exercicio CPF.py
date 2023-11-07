"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF multiplicando cada um dos valores por uma contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: (70+36+48+56+12+20+32+27+0 = 301)
Multiplicar o resultado anterior por 10 (301 * 10 = 3010)
Obter o resto da divisão da conta anterior por 11 (3010 % 11 = 7)
Se o resultado anterior for maior que 9: resultado é 0
contrário disso: resultado é o valor da conta

O primeiro dígito do CPF é 7

"""

cpf = input('Olá! Digite os números do seu CPF: ')
multiplicador = 10
indicador = 0
soma_digito_01 = []
soma_digito_02 = []

### VALIDANDO SOMENTE NÚMEROS SEM PONTUAÇÃO:
if len(cpf) == 11:    

    for digito in cpf:

        ### CONDIÇÃO PARA VALIDAR SOMENTE OS 9 PRIMEIROS CARACTERES (INICIANDO COM ZERO '0')
        if indicador <= 8:
            digito_inteiro = int(digito)
            multiplicacao = multiplicador * digito_inteiro                
            soma_digito_01.append(multiplicacao) ### ADICIONANDO O VALOR DA MULTIPLICAÇÃO NA LISTA PARA CALCULAR O PRIMEIRO DIGITO
            multiplicador -= 1 ### MULTIPLICADOR EM ORDEM DESCRESCENTE
            indicador += 1 ### INDICADOR PARA VALIDAR SOMENTE OS 9 PRIMEIROS CARACTERES  

        ### DEFININDO OS VALORES PARA AS VARIAVEIS E QUEBRANDO O 'FOR'
        else: 
            indicador = 0        
            multiplicador = 11
            break

    ### CALCULANDO O VALOR DO PRIMEIRO DIGITO:
    resto_01 = (sum(soma_digito_01) * 10) % 11
    digito_01 = resto_01 if resto_01 <= 9 else 0

    ### LOOPING PARA CALCULAR O SEGUNDO DIGITO:
    for digito in cpf:

        if indicador <= 9:
            digito_inteiro = int(digito)
            multiplicacao = digito_inteiro * multiplicador
            soma_digito_02.append(multiplicacao)
            multiplicador -= 1
            indicador += 1
        else:
            break

    resto_02 = (sum(soma_digito_02) *10) % 11
    digito_02 = resto_02 if resto_02 <= 9 else 0

    ### CONDIÇÃO PARA RETORNAR SE O CPF É VÁLIDO:

    if digito_01 == int(cpf[9]) and digito_02 == int(cpf[10]):
        print('CPF Válido \n')
    else:
        print('CPF Inválido \n')
        
else:
    print('Caracteres Inválidos! \n')


# cpf = '92371655015'
