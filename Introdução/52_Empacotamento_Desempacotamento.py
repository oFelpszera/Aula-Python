# PODEMOS EMPACONTAR OS ITENS DA LISTA EM VARIAVEIS OU DESEMPACOTAR:

lista = [
    'Felipe', 'Giovanna', 'Haroldo', 'Sueli'
]


# AQUI AUTOMATICAMENTE ELE VAI DESEMPACOTAR A LISTA COLOCANDO EM ORDEM CADA ITEM DENTRO DA VARIAVEL
nome1, nome2, nome3, nome4 = lista
print(nome4) # Sueli


# PODERIAMOS ESPECIFICAR A LISTA DIRETO NO DESEMPACOTAMENTO:
nome1, nome2, nome3, nome4 = ['Felipe', 'Giovanna', 'Haroldo', 'Sueli']
print(nome1)


# SE TIVER MAIS VARIAVEIS DO QUE ITENS, IRÁ GERAR UM ERRO 'ValueError'
# INFORMANDO QUE NÃO TEM ITENS O SUFICIENTE PARA DESEMPACOTAR
nome1, nome2, nome3, nome4 = ['Felipe', 'Giovanna', 'Haroldo']
print(nome1) # not enough values to unpack (expected 4, got 3)


# O INVERSO TABÉM GERARÁ ERRO, SE TIVER MAIS ITENS DO QUE VARIAVEIS 'ValueError'
# INFORMANDO QUE TEM MAIS ITENS DO QUE VARIAVEIS PARA DESEMPACOTAR
nome1, nome2, nome3 = ['Felipe', 'Giovanna', 'Haroldo', 'Sueli']
print(nome1) # too many values to unpack (expected 3)


# É POSSÍVEL DESEMPACOTAR UM ITEM E, EMPACOTAR O RESTO UTILIZANDO '*' ASTERISCO + NOME DA VARIAVEL
nome, *resto = ['Felipe', 'Giovanna', 'Haroldo', 'Sueli']
print(nome, resto) # Felipe ['Giovanna', 'Haroldo', 'Sueli']


# PARA DESEMPACOTAR UM ITEM DO MEIO, DEVEMOS SEGUIR A MESMA LÓGICA NOS ITENS ANTERIORES AO QUE QUEREMOS
# É UMA BOA PRÁTICA USAR UNDERLINE '_' PARA DEFINIR A VARIAVEL DO ITEM QUE NÃO VAMOS UTILIZAR
_, nome, *_ = ['Felipe', 'Giovanna', 'Haroldo', 'Sueli']
print(nome) # Giovanna


# PODEMOS EMPACOTAR AS INFORMAÇÕES ANTES DA ÚLTIMA QUE QUEREMOS
*_, nome = ['Felipe', 'Giovanna', 'Haroldo', 'Sueli']
print(nome, _) # Sueli ['Felipe', 'Giovanna', 'Haroldo']




