"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos,
escreva: "Seu nome é curto.", se tivet entre 5 e 6 letras: "Seu nome é normal", se
for maior que 6: "Seu nome é muito grande."
"""

nome = input('Qual é o seu primeiro nome: ')

caracteres = len(nome)

int_caracteres = int(caracteres) # NÃO PRECISA - len JA RETORNA INT

nome_curto = int_caracteres <= 4
nome_normal = int_caracteres >= 4 and int_caracteres <= 6
nome_grade = int_caracteres > 6

if ' ' not in nome:   

    if nome_curto:
        print('Seu nome é curto. ', end='\n\n')
    elif nome_normal:
        print('Seu nome é normal. ', end='\n\n')
    elif nome_grade:
        print('Seu nome é grande. ', end='\n\n')

else:
    print('Seu nome contém espaços.', end='\n\n')

# ELE UTILIZOU OUTRO IF INFORMANDO QUE O NOME DEVE SER MAIOR QUE UMA LETRA "if caracteres > 1"
# NÃO PRECISA CONVERTER PARA INT, POIS A VARIAVEL COM 'LEN' JA RETORNA 'INT' -- AULA 57
