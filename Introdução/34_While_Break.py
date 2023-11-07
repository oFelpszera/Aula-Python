# WHILE (Enquanto) - Executa uma ação em loop enquanto uma condição é atendida.
# Devemos tomar cuidado para não criar um loop infinito que é quando a condição é sempre atendida, sem fim. 
# Exemplo:

condicao = True

while True:
    nome = input('Qual é o seu nome: ')
    print(f'Seu nome é {nome}')

# Isso iria se repetir infinitamente, pois a condição é sempre TRUE (Verdadeira). 
# Para quebrar isso, utilizamos o BREAK 
# Podemos ter um WHILE dentro de outro WHILE, então o BREAK quebra o WHILE mais próximo. 

    # break <- ATIVAR PARA PARAR O CÓDIGO E LIBERAR A EXCUÇÃO DO 'PRINT' ABAIXO.

print('123') # CODE IS UNREACHABLE PYLANCE = Código não alcaçável. Pode ocorrer isso, pois ele identifica que o loop será infinito.

    