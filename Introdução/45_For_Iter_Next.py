



### ASSISTIR AULA 74 DA SESSÃO 03 - FOR POR BAIXO DOS PANOS

""" 

BASICAMENTE EXISTE ALGUNS COMANDOS MANUAIS QUE O FOR FAZ AUTOMATICAMENTE.

Temos os objetos ITERAVEIS que podem ser strings, range etc.
Temos o ITERADOR que é entregador que busca a string na memória, para entregar os valores -> .__iter__() ou iter()
Temos o NEXT que busca o proximo valor -> .__next__() ou next()

"""

texto = 'Felipe' # Meu objeto ITERAVEL
iterador = iter(texto) # ITERADOR que vai identificar o objeto iteravel (STRING) na memória, poderia ser -> iterador = texto.__iter__()

while True:
    try:
        letra = next(iterador) # Buca a próxima letra do ITERADOR que é o ENTREGADOR da STRING 'Felipe', poderia ser -> letra = iterador.__next__()
        print(letra)
    except StopIteration:
        break

        # É necessário usar o TRY/EXCEPT pois em algum momento haverá um erro, pois não vai existir uma PRÓXIMA letra.
    
# EM RESUMO É ISSO QUE O FOR FAZ, CHAMA O ENTREGADOR DA STRING GUARDADA NA MEMORIA (ITERADOR),
# CHAMA AS PROXIMA LETRAS (NEXT)
# E PARA QUANDO APRESENTA O ERRO (STOPITERATION)

# O FOR RESUME O CÓDIGO ACIMA:

print('\n') # Apenas dando um espaço nas linhas

for letra in texto:
    print(letra)

    