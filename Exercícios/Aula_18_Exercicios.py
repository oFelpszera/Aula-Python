# EXERCÍCIO DE INPUT E COMPARAÇÃO

valor_01 = input('Digite um valor: ')
valor_02 = input('Digite outro valor: ')
print(end=('\n\n'))

int_01 = int(valor_01)
int_02 = int(valor_02)

if int_01 > int_02:
    print(f'O primeiro valor {valor_01}, é maior que o segundo valor {valor_02}', end='\n\n')
elif int_01 < int_02:
    print(f'O segundo valor {valor_02}, é maior que o primeiro valor {valor_01}', end='\n\n')
else:
    print(f'O primeiro valor {valor_01} e, o segundo valor {valor_02}, são iguais', end='\n\n')



