"""
COMPLEMENTO DO EXERCICIO DE VALIDAR CPF

EXISTEM ALGUNS PROBLEMAS QUE PODEM APARECER NO ALGORTIMO:

1. O usuário poderia mandar números com pontos e traço, para isso podemos usar o REPLACE para substitui-los;
2. O usuário poderia mandar letras, então podemos usar uma REGULAR EXPRESSION com IMPORT RE .sub(r'padrão', 'alteração', string);
3. O usuário poderia repetir os números, o que geraria CPF Válido (000.000.000-00).

"""

### 1 - REPLACE:
cpf = input('Olá, digite os números do seu CPF: ') \
    .replace('.', '')\
    .replace('-', '')

print(cpf)


### 2 - REGULAR EXPRESSION:
import re

cpf = input('Olá, digite os números do seu CPF: ')
regular_expression = re.sub(
    r'[^0-9]', '', cpf ) ### Estou informando que tudo o que não for digito de 0 à 9 será substituido por nada ''

print(regular_expression) 


### 3 - REPETIÇÃO:
import sys ### IMPORTA AÇÕES DO SISTEMA, ONDE PODEMOS SAIR DO PYTHON USANDO EXIT

cpf = input('Olá, digite os números do seu CPF: ')
cpf_repetido = cpf[0] * len(cpf) # PEGANDO A PRIMEIRA LETRA E REPETINDO
print(cpf_repetido)

if cpf == cpf_repetido:
    print('Caracteres Repetidos! \n')
    sys.exit()




 ### VARIAVEIS  

digitos_cpf = cpf[:9]
multiplicador_digito_01 = 10
soma_digito_01 = 0

### LOOPING PARA VALIDAR PRIMEIRO DIGITO:

for digito in digitos_cpf:
    soma_digito_01 += int(digito) * multiplicador_digito_01
    multiplicador_digito_01 -= 1
resto_01 = ((soma_digito_01 * 10) % 11)
digito_01 = resto_01 if resto_01 <= 9 else 0

### LOPPING PARA VALIDAR SEGUNDO DIGITO:

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