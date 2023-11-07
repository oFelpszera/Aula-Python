# CONCATENAÇÃO COM "+" E REPETIÇÃO COM "*"

concatenacao_01 = 'Felipe' + ' ' + 'Andrade'
# Será unido as duas informações mais o espaço ' ' - Type - "str"
print(concatenacao_01)

concatenacao_02 = 'Felipe' + ' ' + str(23)
# Será concatenado os valores, usei str(23) para converter o "int" 23
print(concatenacao_02)

repeticao_01 = ('Felps' + ' ') * 3
# Será repetido a informação 3x, coloquei espaço para não grudar
# Necessário colocar entre parenteses para multiplicar todo o conjunto
print(repeticao_01)

repeticao_02 = ('Felps' + ' ' + str(23) + ' ') * 3
# Será repetido a informação mais núm convertido para "str"
# Sem o parenteses, multiplica somente a última info. str(23)
print(repeticao_02 )

