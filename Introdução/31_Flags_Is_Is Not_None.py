# AULA CONFUUUUUUUSA, MAS VAMOS LÁ
# FLAG (Bandeira) - Quando você "marca" um lugar no código com o valor que quer.
# NONE = Não Valor
# IS e IS NOT = É e NÃO É (Tipo, Valor, Identidade'ID')

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True # Flag informando que o valor tem que ser 'True'.
    print('Passou no IF. ')
else:
    print('Não Passou no IF. ')

print(f'{passou_no_if} é NONE: {passou_no_if is None}')
print(f'{passou_no_if} não é NONE: {passou_no_if is not None}')
print('\n')

"""
É um pouco confuso, mas eu tenho uma condição que se for executa, vai mudar minha variável
'passou_no_if' era NONE, mas como a 'condicao' é TRUE, ele passou a ser 'TRUE'.
Pos isso, TRUE é NONE = FALSE // TRUE não é NONE = TRUE

Se a 'condicao' fosse FALSE, não executaria o IF, logo o 'passou_no_if', continuaria sendo NONE.
O que resultaria NONE não é NONE = FALSE // NONE é NONE = TRUE

"""