# iNTRODUÇÃO A "f-strings" -> Formatação de Texto
# Serve para formatar o comando dentra da "variável" e pedir "print" somente da variável.
# Para isso, usamos "f", tudo o que for variável colocamos chaves "{}"

nome = 'Felipe Andrade'
peso = 78.65
altura = 1.80
imc_01 = peso / altura ** 2

variavel_01 = f'{nome} tem {altura} de altura,'
variavel_02 = f'pesa {peso} quilos e seu IMC é:'
variavel_03 = imc_01

print(variavel_01)
print(variavel_02)
print(variavel_03, end='\n\n') # Pedi duas quebras de linhas \n\n

# Para formatar casas decimais, após a variável usamos ":.2f"
# Nesse caso vai separa por ponto "." com 2 casas decimais após.

variavel_04 = f'{nome} tem {altura:.2f} de altura,'
variavel_05 = f'{imc_01:.2f}'

print(variavel_04)
print(variavel_05, end='\n\n')



