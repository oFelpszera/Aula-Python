# INTRODUÇÃO AO TRY-EXCEPT (Função usadas juntas)
# TRY = Ele 'Tenta' executar o código
# EXCEPT = Se houver algum erro ele executa o código da 'Exceção'
# FAIL FAST = Errar Rápido.
# Em resumo se houver algum erro no Try, ele exceuta direto o Except sem apresentar o erro.
# .isdigit = Informa que a variável tem que ser um dígito inteiro (sem ponto, sem letra)

numero = input('Digite um número: ')
if numero.isdigit(): # Só considera número inteiro, sem ponto, virgula ou letra.
    print('Seu número é: ', numero)
else:
    print('Isso não é um número', end='\n\n')

numero_01 = input(
    'Agora digite um número para eu dobrar: '
    )

try:
    numero_float = float(numero_01)
    print('Seu número é: ', numero_01)
    print(f'O dobro desse número é: {numero_float * 2}', end='\n\n') 
except:
    print('Este não é um número válido.', end='\n\n')

# Ao selecionar um código e apertar F2, renomeamos todos com o mesmo nome.

# PARA DÚVIDAS SOBRE ESSA AULA, ACESSAR O DOCUMENTO DO WORD COM MAIS DETALHES

