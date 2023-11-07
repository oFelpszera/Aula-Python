# FORMATAÇÃO DE STRINGS COM 'FORMAT'
# .format é um "Méthod" que permite fomartar os dados dentro de chaves {}
# Ele pode ser chamado pela sequência dos "Argumentos" ou podemos utilizar "Parametros Nomeaveis"
# Para puxar a inforação do Argumento dentro de format, não dar espaço 'a={}'

a = 'Salário'
b = 'Felipe Andrade'
c = 15000

argumento = '0: a={} b={} c={}' # Ele vai puxar os Argumentos por sequência dentro do .format
formato = argumento.format(a, b, c)
print(formato, end='\n\n') 

argumento_01 = '1: a={} b={} c={:,.2f}' # Estou formatando os números com ',' e '.'
formato = argumento_01.format(a, b, c)
print(formato, end='\n\n') 

argumento_02 = '2: a={1} b={0} c={2:,.2f}' # Estou definindo a sequencia que quero chamar
formato = argumento_02.format(a, b, c) # Sempre inicia a contagem do "0" -> a=0 b=1 c=2
print(formato, end='\n\n') 

argumento_03 = '3: a={nome1} b={nome0} c={nome2:,.2f}' # Agora dei nome aos argumentos (a, b, c)
formato = argumento_03.format(nome0=a, nome1=b, nome2=c) 
# Se nomear o primeiro Argumento, todos em seguida devem ser nomeados.
# Se nomear o último Argumento, os anteriores não precisam estar nomeados.
print(formato, end='\n\n')

