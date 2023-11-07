""" FOR IN É MAIS UTILIZADO PARA QUANDO SABEMOS ONDE O LAÇO COMEÇA E TERMINA,
DIFERENTE DO WHILE, ONDE PODE SER INFINITO O NÚMERO DE REPETIÇÕES, POR EXEMPLO UMA DIGITAÇÃO DE SENHA:
"""

senha = '123456'
senha_digitada = ''
repeticoes = 0

while senha_digitada != senha:
    senha_digitada = input(f'Você tentou ({repeticoes}x) ')
    repeticoes += 1 

print('Parabéns, senha correta!')

# Nesse exemplo acima, o numero de repetições de senha pode ser infinito, por isso usamos o WHILE (Enquanto).

# Já para o FOR IN, por saber que tem um fim, fica mais fácil:

texto = 'Hello, World!'
letra_asterisco = ''

for letra in texto:
    letra_asterisco += f'*{letra}'
    print(letra)
print(f'{letra_asterisco}' + '*')