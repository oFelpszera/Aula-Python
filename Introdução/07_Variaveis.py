# VARIÁVEIS: São usadas para salvar um comando específico para depois utilizar somente o 'titulo' dela.
# PEP8: Ininicie variáveis com letras minúsculas, podendo usar números e underline.
# O sinal de "=" é o "operador" que atribui o comando para o 'titulo' usado.
nome_completo = 'Haroldo Felipe Fernandes de Andrade' # O 'titulo' da variável é 'nome_completo'
apelido = 'Felps' # O 'titulo' da variável é 'apelido'
idade = 30 # 'titulo' da variável é 'idade'
maior_de_idade = idade >= 18 # Aqui tem a variável '>=' que retorna se é maior ou igual "X"
# Agora não tem necessidade de escrever os dados, mas sim chamar os 'titulos' das variáveis
print('Nome:', nome_completo) # Haroldo Felipe Fernandes de Andrade
print('Apelido:', apelido) # Felps
print('Idade:', idade) # 30
print('É maior de idade?:', maior_de_idade, end="\n\n") # True
"""
Uma das vantagens de se utilizar variáveis é poder alterar vários dados sem necessidade
de alterar um por um, basta alterar o resultado do 'titulo
"""
numero = 23.0
tipo = type(23.0)
nome = 'Felps'
tipo_nome = type('')
print(numero, tipo) 
print(nome, tipo_nome) # Usei 'end="\n\n"' para pular a linha duas vezes
print('O Apelido dele é:', nome, 'Ele percorre:', numero, 'KM/h', end=".\n\n")