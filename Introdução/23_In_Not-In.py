# OPERADORES "IN" E "NOT IN"
# SÃO OPERADORES PARA SABER SE ALGUMA INFORMAÇÃO ESTÁ DENTRO DO DADO OU NÃO
# STRINGS "STR" SÃO ITERAVEIS - NAVEGAR ITEM POR ITEM
#  0  1  2  3  4  5
#  F  E  L  I  P  E
# -6 -5 -4 -3 -2 -1 
# NAVEGANDO ITEM POR ITEM EU CONSIGO PUXAR ALGUMA LETRA ESPECÍFICA
# DO 0 DA ESQ. PARA DIR. OU -1 DA DIR. PARA ESQ.

nome = 'FELIPE'
print(nome[2]) # Vai ler a letra "L"
print(nome [-5]) # Vai ler a letra "E"
print(10 * '-')

print('LIPE' in nome) # LIPE está em NOME? - TRUE
print('FELPS' not in nome) # FELPS não está em NOME? - TRUE
print('FELPS' in nome) # FELPS está em NOME? - FALSE
print('FE' not in nome) # FE não está em NOME? - FALSE
print(10 * '-')

nome_01 = input('Digite Algo: ')
print(end='\n')
nome_02 = input('Digite sua busca dentro desse algo: ')
print(end='\n')
if nome_02 in nome_01: # Se a busca 'estiver dentro' do "nome_01"
    print(f'{nome_02} está em {nome_01}', end='\n\n')
elif nome_02 not in nome_01: # Se a busca 'não estiver dentro' no "nome_01"
    print(f'{nome_02} não está em {nome_01}', end='\n\n')




