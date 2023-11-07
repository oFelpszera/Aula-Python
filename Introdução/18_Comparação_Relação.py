# OPERADORES DE COMPARAÇÃO (RELACIONAIS)
"""
OPERADOR        SIGNIFICADO         EXEMPLO (TRUE/FALSE)
>               Maior               2 > 1
>=              Maior ou Igual      2 >= 3 -> Essa será "False"
<               Menor               1 < 2
<=              Menor ou Igual      1 <= 1
==              Igual               'a' == 'A'  -> Essa será "False"
!=              Diferente           'a' != 'A'
"""

maior = 2 > 1
maior_ou_igual = 2 >= 3
menor = 1 < 2
menor_ou_igual = 2 <= 2
igual = 'a' == 'A'
diferente = 'a' != 'A'

print(maior, maior_ou_igual, menor, menor_ou_igual, igual, diferente, sep='\n', end='\n\n')

# Eu posso abrir o módulo no Power Shell do Windows e, escrever as variáveis para
# colher os resultados, sem precisar dar "print", basta ir no Terminal
# conferir a pasta que estou digitando "pwd" depois "ls" 
# e digitar "python -i 'caminho da pasta'"

