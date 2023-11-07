"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito,
exiba a saudação apropriada. Ex.:
Bom dia (0-11) - Boa tarde (12-17) - Boa noite (18-23)
"""
horas = input('Que horas são?: ')
horas_int = int(horas)

bom_dia = horas_int >= 0 and horas_int <= 11
boa_tarde = horas_int >= 12 and horas_int <= 17
boa_noite = horas_int >= 18 and horas_int <= 23

if horas.isdigit():

    if bom_dia:
        print('Bom dia!', '\n\n')
    elif boa_tarde:
        print('Boa tarde!', '\n\n')
    elif boa_noite:
        print('Boa noite!', '\n\n')
    else:
        print('Não conheço essa hora', end='\n\n')

else:
    print('Hora inválida!', end='\n\n')

# NA AULA 56 DA RESOLUÇÃO ELE USOU TRY / EXCEPT