# TUPLES ou TUPLAS -> SÃO LISTAS TAMBÉM, PORÉM IMUTAVEIS.
# OU SEJA, NÃO É POSSÍVEL ALTERAR IGUAL UMA LISTA NORMAL QUE É IMUTAVEL.

# EXISTEM ALGUAMS MANEIRAS DE SE CRIAR TUPLAS:

# A PRIMEIRA É APENAS INFORMANDO OS ITENS QUE TERÁ NELA:

tupla_01 = 'Felipe', 'Giovanna', 23, True 
print(tupla_01)

# UMA LISTA RETORNA DENTRO DE COLHETES [] JÁ AS TUPLAS RETORNA DENTRO DE PARENTESES ()
# LOGO PODEMOS DEFINIR ISSO:

tupla_02 = ('Felps', 'Haroldo', 'Sueli', 1955)
print(tupla_02)

# OUTRA MANEIRA É CONVERTENDO UMA LISTA EM TUPLAS OU VISE-VERSA:

lista = ['Felps Andrade', 23, 'Data Analyst', True]
tupla_03 = tuple(lista)
print(tupla_03 )

lista_01 = list(tupla_03)
print(lista_01, '\n') # Aqui vai retornar dentro de colchetes, pois é uma Lista Mutável

