# OPERADORES LÓGICOS -> "AND" (E), "OR" (OU), "NOT" (NÃO)
# "OR" - Qulaquer condição pode ser "VERDADEIRA"
# Se qualquer valor for condirado "VERDADEIRO", a expressão inteira será avaliada "VERDADEIRA"
# TRUTHY - é um valor neutro 0, 0.0, '' (sem espaço), pois representa "nada"
# NONE - também represenda "nada", é um "não valor"

entrada = input('Digite [E] Entrar ou [S] Sair: ')
nome_permitido = 'Felipe Andrade'
senha_permitida = '123456'

if entrada == 'E' or entrada == 'e':
    print(end='\n')
    nome = input('Digite seu Nome: ')
    if nome == nome_permitido:
        print(end='\n')
        senha = input('Digite uma Senha: ')
        if (entrada == 'E' or entrada == 'e') and nome == nome_permitido and senha == senha_permitida:
            print('Parabéns, você está logado! ', end='\n\n')
        elif senha == '':
            print('Senha Não Digitada! ', end='\n\n')
        else:
            print('Senha Incorreta! ', end='\n\n')
    elif nome == '':
        print('Nome Não Digitado! ', end='\n\n')
    else:
        print('Nome Incorreto! ', end='\n\n')
elif entrada == '':
     print('Você não digitou "E" ou "S"', end='\n\n')
elif entrada == 'S' or entrada == 's':
    print('Você Está Deslogado! ', end='\n\n')
else:
     print('Você não digitou um carácter válido! ', end='\n\n')


    


    