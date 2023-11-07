# USANDO FUNÇÃO INPUT PARA COLETAR DADOS DO USUÁRIO

nome = input('Qual o seu Nome? ')
sobrenome = input('Qual o seu sobrenome? ') 
print(f'Seja bem-vindo(a) {nome} {sobrenome},', end='\n') 
pergunta = input('Quantos anos vocês tem? ')
print(end='\n') 
print('Certo. Vamos iniciar o cálculo do seu IMC.', end='\n\n')

altura = input('Qual a sua altura? ')
peso = input('Qual é o seu peso? ')
float_01 = float(altura)
float_02 = float(peso)
print(f'{nome}, seu IMC é: {float_02 / (float_01 * float_01):.2f}', end='\n\n')

