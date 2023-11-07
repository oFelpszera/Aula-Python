# APENAS UMA AULA PARA INFORMAR QUE O ELSE, BREAK E CONTINUE É POSSÍVEL UTILIZAR NO FOR IGUAL NO WHILE:

numeros = range(10)

for i in numeros: # i = indice - muito comum essa utilização

    if i == 2:
        print('Não vou mostrar o número 2')
        continue

    if i == 8:
        print('Não vou mostrar o 8 e, vou parar o FOR antes do ELSE')
        break 
        # Se eu alterar o BREAK por CONTINUE, meu ELSE abaixo será executado.

    print(i)

else:
    print('FOR completado com sucesso.')