# FORMATAÇÃO BÁSICA DE STRINGS COM "f-strings"
# (s) string - (d ou i) int - (f) float
# <número de dígitos ou caractéres antes ou depois do dado>f
# (<) Preenche para direita - (>) Preenche para esquerda - (^) Preenche para o centro
# Sinal "-" ou "+" ou "-+" para mostrar no print. Ex: 0>-100,.2f
# (Preenche de zero do lado esquerdo, mostra o sinal "-" 100.00)

variavel = 'oFelps'
print(f'{variavel:x>10}') # Preenche "x" a esquerda com total de 10 caractéres
print(f'{variavel:X<10}') # Preenche "X" a direita com total de 10 caractéres
print(f'{variavel:#^10}') # Preenche "#" deixando a variável no centro com total de 10 caractéres
print(f'{variavel: ^10}') # Preenche com espaço.

preco = 2322335.5654488
print(f'R${preco:,.2f}') # Mostra o preço com "," "." "2 casas decimais"
print(f'{preco:+,.2f}') # Mostra o preço com com sinal de "+" SE ELE FOR POSITIVO
print(f'{-235555.22:+,.2f}') # Mostra o valor com com sinal de "-" SE ELE FOR NEGATIVO

print(f'O Hexadecimal de 23000 é {23000:08X}.')
# 08X Hexadecimal maiusculo preenchidos por "0" totalizando 8 caracteres
print(f'O Hexadecimal de 23000 é {23000:8x}.')
 # 8x Hexadecimal minusculo preenchidos por "espaço" totalizando 8 caracteres
print(f'O Hexadecimal de 23000 é {23000:X}.')
 # X Hexadecimal sem preenchimento.
print(f'O Hexadecimal de 23000 é {23000:<08X}.')
# <08X - Hexadecimal preenchidos com "0" a direita totalizando 8 caracteres
print(f'O Hexadecimal de 23000 é {23000:^10X}.')
# ^10X - Hexadecimal preenchidos centralizado totalizando 10 caracteres
print(f'O Hexadecimal de 23000 é {23000:>10X}.')
# ^10X - Hexadecimal com espaço a esqueda totalizando 10 caracteres
print(end='\n\n')

