# CALCULADORA COM WHILE

# FOI APRESENTADO DOIS METHODs O .lower() QUE RETORNA UMA 'STR' EM LETRAS MINUSCULAS E,
# .startswith('') QUE INFORMA COM QUE LETRA O TEXTO COMEÇA OU, .endswith('') QUE INFOMRA QUAL LETRA TERMINA -> 'BOOL'

print('Olá, seja bem-vindo a Calculadora em Python!' '\n')

nome = input('Qual é o seu nome: ').capitalize() # RETORNA A PRIMEIRA LETRA EM MAIÚSCULO
inicio = print(f'Certo {nome}, vamos começar!' '\n')

while True:
    
    try:
        num1 = float(input('Digite um número: '))
        num2 = float(input(f'{nome}, digite outro número: '))
        operador = input('Escolha um operador: [+], [-], [/], [*]: ')
        num_valido = True
    except:
        num_valido = None
        print('Número inválido! Digite Novamente.' '\n\n')
        continue        
    
# SOMA
    if operador == '+':
        print(f'O resultado da Soma é: {num1 + num2}, \n')

# SUBTRAÇÃO
    elif operador == '-':
        print(f'O resultado da Subtração é: {num1 - num2}, \n')

# DIVISÃO
    elif operador == '/':
        print(f'O resultado da Divisão é: {num1 / num2}, \n')

# MULTIPLICAÇÃO
    elif operador == '*':
        print(f'O resultado da Multiplicação é: {num1 * num2}, \n')
    
    else:
        print('Operador Inválido! Digite Novamente.' '\n\n')
        continue

    sair = input('Deseja finalizar a Calculadora em Python? ').capitalize().startswith('S')
    print('\n')
    if sair is True:
        break

print('Obrigado por participar!' '\n\n')