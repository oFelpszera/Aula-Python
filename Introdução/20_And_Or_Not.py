# OPERADORES LÓGICOS -> "AND" (E), "OR" (OU), "NOT" (NÃO)
# "AND" - Todas as condições precisam ser "VERDADEIRAS"
# Se qualquer valor for condirado "FALSO", a expressão inteira será avaliada "FALSO"
# FALSY - é um valor entre aspas falso, pois representa "nada"
# NONE - também represenda "nada", é um "não valor"

entrada = input('Digite [E] Entrar ou [S] Sair: ')
nome_permitido = 'Felipe Andrade'
senha_permitida = '123456'

if entrada == 'E':
    print(end='\n')
    nome = input('Digite o seu Nome: ')

    if entrada == 'E' and nome == nome_permitido:
        print(end='\n')
        senha = input('Digite uma senha: ')
        if entrada == 'E' and nome == nome_permitido and senha == senha_permitida:
            print('Você está logado.', end='\n\n')
        elif senha != senha_permitida:
            print('Senha incorreta!', end='\n\n')
    elif nome != nome_permitido:
            print('Nome Incorreto! ', end='\n\n')
elif entrada == '':
     print('Você não digitou "E" ou "S"', end='\n\n')
else:
    print('Você está deslogado!', end='\n\n')


