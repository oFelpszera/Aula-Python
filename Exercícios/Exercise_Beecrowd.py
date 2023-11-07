# MÉDIA PONDERADA
# MULTIPLICA-SE A NOTA PELO VALOR DO PESO E DIVIDE PELA SOMA DOS PESOS

weight_A = 3.5
weight_B = 7.5

A = float(input())
B = float(input())

media = ((A * weight_A) + (B * weight_B)) / (weight_A + weight_B)
print(f'MEDIA = {media:.5f}')


# NOTA MÉDIA PONDERADA COM 3 ARGUMENTOS OBRIGATORIAMENTE MENOR QUE 10

weight_A = 2
weight_B = 3
weight_C = 5

A = float(input())
B = float(input())
C = float(input())

media = (
    ((A * weight_A) +
    (B * weight_B) +
    (C * weight_C)) /
    (weight_A + weight_B + weight_C)
    )

if A > 10 or B > 10 or C > 10:
    print('Nota inválida!')
else:
    print(f'MEDIA = {media:.1f}')

# CALCULANDO DIFERENÇA (VALOR MENOS OUTRO VALOR):

A = int(input())
B = int(input())
C = int(input())
D = int(input())

diference = ((A * B) - (C * D))

print(f'DIFERENCA = {diference}')