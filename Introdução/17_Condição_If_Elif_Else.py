# CONDIÇÕES COM "IF" = SE   //   "ELIF" = SE NÃO SE   //    "ELSE" = SE NÃO
# Podemos usar o "if" sozinho, mas o "elif" e "else" não, pois dependem do "if"
# REVIEW - Podemos ter quantos "elif" quisermos para dar a condição

condicao_01 = False
condicao_02 = False
condicao_03 = 10 == 10 # A condição pode ser algum retorno igual
condicao_04 = False 

# Quando o "if", "elif", "else" encontrar uma condição verdadeira, irá me retornar o comando

if condicao_01: # Se condicao_01 for verdadeira ":" então...
    print('Condição 01 é verdadeira.')
elif condicao_02:
    print('Condição 02 é verdadeira')
elif condicao_03:
    print('Condição 03 é verdadeira')
elif condicao_04:
    print('Condição 04 é verdadeira')
else:
    print('Nenhuma das Condições são verdadeiras')    

# Sempre será executado uma única condição, se a 02 e 03 forem verdadeiras, 
# somente a 02 que é a primeira, será executada. Se quiser que outras sejam, basta
# usar outro "if" depois das condições "elif" e "else"

