# FATIAMENTO DE STRINGS "str"
#  0 à 13
#  Felipe Andrade
# -14 à -1 
# FATIAMENTO: [i : f : p] [::] -> (i) Inicio -> (f) Fim -> (p) Passo
# len() retorna a quantidade de caracteres da string "str"

variavel = 'Felipe Andrade'

print('Qtd. Caracteres na variável: ', len(variavel), end='\n\n') 
# Vai me dizer que a variavel "Felipe Andrade" tem 14 caracteres (conta o espaço)
print('Qtd. Caracteres no intervalo "6": ', len(variavel[6]), end='\n\n') 
# Vai me dizer que o caracter "6" (espaço) representa 1 caracter
print('Qtd. Caracters no intervalo de 2 à 13: ', len(variavel[2:13]), end='\n\n') 
# Vai me dizer que do inicio "2" ao fim "13" existem 11 caracteres, inicia no 3º
print('Resultado do inicio ao fim: ', variavel[::], end='\n\n') 
# Vai me trazer o resultado [::] do inicio ao fim // Felipe Andrade
print('Resultado do intervalo 2 ao 10: ', variavel [2:10], end='\n\n') 
# Vai me trazer o resultado do inico "3" ao fim "10" - o último não aparece // lipe And
print('Resultado do inicio ao intervalo 6, com passo 2: ', variavel[:6:2], end='\n\n') 
# Vai me trazer o resultado do inicio ":" ao fim "6" com passo de "2" caracteres // Flp
print('Resultado do fim ao intervalo -8 com passo -1: ', variavel[:-8:-1], end='\n\n') 
# Vai me trazer o resultado de -14 a -8 com passo -1 // edardnA
print('Resultado do fim para o inicio com passo negativo: ', variavel[::-1],
     end='\n\n') 
# Resultado de traz para frente, não precisa informar os números, 
# pois o passo está inverso.
print('Resultado do intervalo -14 ao -8: ', variavel[-14:-8], end='\n\n') 
# Resultado Felipe utilizando o inicio negativo

