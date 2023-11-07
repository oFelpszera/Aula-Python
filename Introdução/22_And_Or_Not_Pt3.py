# OPERADORES LÓGICOS -> "AND" (E), "OR" (OU), "NOT" (NÃO)
# "NOT" - Qulaquer condição "TRUE" vira "FALSE" e, qualquer condição "FALSE" vira "TRUE".
# Ele inverte a expressão.

entrada1 = input('Digite uma senha: ')
print('\n')
entrada2 = input('Confirme a senha: ')
print('\n')

if not entrada2 == entrada1: # Aqui ele inverte, ou seja, não pode ser senhas iguais.
    print('Senhas Divergentes! ', end='\n\n')
    if entrada1 == '' or entrada2 == '':
        print('Digite uma senha válida! ', end='\n\n')
elif entrada1 == '' and entrada2 == '':
    print('Digite uma senha! ', end='\n\n')
else:
    print('Senha Aprovada! ', end='\n\n')


