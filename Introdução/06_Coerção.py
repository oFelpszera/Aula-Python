"""
CONVERSÃO DE TIPOS - COERÇÃO
Podem ser chamados de: "Type Convertion", "Typecasting", "Coercion"
É o ato de converter um tipo (str, int, float, bool) que são tipo "Imutáveis", em outro
"""
print(1, 1 + 1, sep='- ') # 1- Aqui ele vai concatenar dois "int" = 2
print(2, 'a' + 'b', type('a' + 'b'), sep='- ') # 2- Aqui ele vai concatenar dois "str" = ab
# print(1 + 'b') // Aqui ele me resultaria um erro, dizendo que não pode concatenar "int" com "str"
print(3, str('1') + 'b', sep='- ') # 3- Aqui eu converti o "1" para "str" para concatenar com "b" = 1b
print(4, 1 + float('1'), sep='- ') # 4- Aqui eu converti o "1" que é "str" pois está com aspas, em "float" = 2.0
print(5, bool(""), sep='- ') # 5- Aqui eu converti a informação "" em "False", se tivesse espaço " ", seria "True"


