"""
DOCUMENTAÇÃO PYTHON - TIPOS EMBUTIDOS - IMUTAVEIS
https://docs.python.org/pt-br/3/library/stdtypes.html

IMUTAVEIS -> "str", "float", "int", "bool" - Existem outros que ainda não vimos.

Ações apresentadas de Método str -> .zfill (preenche com zero a esquerda,
totalizando o número de caractéres escolhido); .capitalize (traz a primeira letra "Maiuscula")

"""

variavel_imutavel = 'felipe andrade'
# O nome da variavel pode ser alterado, mas o resultado não conseguimos fazer alteração, 
# No caso acima, não é possível pedir para trocar uma letra por outra, por isso é imutavel.
# Caso eu queria trocar uma letra, poderia utilizar fatiamento com f-strings.

variavel_alteracao = f'{variavel_imutavel[:3]}ps{variavel_imutavel[6:]}' 
# felps andrade / Só foi possível alterar pois criamos uma NOVA VARIAVEL a antiga continua igual. 
print(variavel_alteracao)

print(variavel_alteracao.capitalize()) # É uma METHOD, por isso precisa de parenteses ao final

print(variavel_alteracao.zfill(23)) # Preenche com ZERO a esqueda. Defini 23 caracteres contando com o nome

print(len(variavel_alteracao)) # Saber quantos caracteres minha variavel tem (13)

print(variavel_alteracao.capitalize().zfill(15)) # Primeira letra maiuscula + 2 zeros a esquerda coloquei 15, pois de nome tem 13 caracteres.

print('\n')


