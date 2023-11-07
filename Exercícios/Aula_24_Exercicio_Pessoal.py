"""
O sistema hexadecimal utiliza 16 símbolos, letras ABCDEF e números 0123456789
Chama Hexadecimal pois tem 6 letras e, 10 números.

"""
print('Vamos descobrir o valor Hexadecimal de sua Data de Nascimento:', end='\n\n')
dia = input('Digite o dia (XX) do seu nascimento: ')


dias = ('0,01,02,03,04,05,06,07,08,09,'
        '10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31')
meses = '01,02,03,04,05,06,07,08,09,10,11,12'

if dia in dias:
    mes = input('Digite o mês (XX) do seu nascimento: ')
    if mes in meses:
        ano = input('Digite o ano (XXXX) do seu nascimento: ')
        print('\n')

        int_dia = int(dia)
        int_mes = int(mes)
        int_ano = int(ano)

        soma = int_dia + int_mes + int_ano
        print(f'O Hexadecimal da sua data de nascimento é {int_dia:05X}')
        print(f'O Hexadecimal do seu mês de nascimento é {int_mes:05X}')
        print(f'O Hexadecimal do seu ano de nascimento é {int_ano:05X}', end='\n\n')
        print(f'A soma da sua data de nascimento é {soma} '
              f'e o Hexadecimal da soma do seu nascimento é {soma:05X}', end='\n\n')
    else:
        print('Mês digitada não é válido.', end='\n\n')
else:
    print('Dia digitado não é válido.', end='\n\n')




