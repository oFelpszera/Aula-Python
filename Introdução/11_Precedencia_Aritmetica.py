# PRECEDENCIA ENTRE OPERADORES ARITMÉTICOS

# Sequência em que a leitura é feita:
# 1º O que está entre parenteses -> (n + n)
# 2º O que elevando -> **
# 3º O que está mult., div., div. int., e modulo -> * / // %
# 4º O que está somando e subtraindo -> + -

conta_01 = 1 + 1 ** 5 + 5
# Aqui retorna 7, pois faz 1 sobre 5 primeiro e depois soma tudo
print(conta_01)

conta_02 = (1 + 1) ** (5 + 5)
# Aqui retorna 1024, pois primeiro executa os parenteses.
print(conta_02)

conta_03 = (1 + (0.5 + 0.5)) ** (5 + (3 + 2))
print(conta_03)
# Aqui também retorna 1024, seguindo a regra dos parenteses de dentro
# para fora e, executando os comandos, no caso "adição"

conta_04 = (1 + int(0.5 + 0.5)) ** (5 + (3 + 2))
print(conta_04)
# conta_03 retornou como "float" 1024.0
# Então converti para inteiro "int" os números 0.5 

