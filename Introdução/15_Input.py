# USANDO FUNÇÃO INPUT PARA COLETAR DADOS DO USUÁRIO

nome = input('Qual o Seu Nome? ') # Defini a variável e o 'input' para coletar o dado
print(f'Olá {nome},', end=' ') # Imprimi o dado que o usuário digitou
pergunta = input('quantos anos vocês tem? ') # Fiz outra variável com outro 'input'
print('Certo, vamos começar!', end='\n\n') 

numero_01 = input(f'{nome}. Digite um número: ')
numero_02 = input('Agora digite outro número: ')
print(f'A concatenção dos dois números é: {numero_01 + numero_02}',)
# Aqui ele vai concatenar, pois o 'input' trabalha com "str" e número é "int"
# Então precisamos fazer a coerção de "str" para "int"

int_01 = int(numero_01)
int_02 = int(numero_02)
print(f'A soma dos dois números é: {int_01 + int_02}', end='\n\n' )
# Criei outra variável para a coerção, pois se eu converto direto no "input", caso o usuário
# digite uma letra "str", ao invés de número "int", ocorrerá um erro impedindo a checagem do dado.

print('Agora vamos cálcular o seu IMC:')
altura = input('Qual a sua altura? ')
peso = input('Qual é o seu peso? ')
float_01 = float(altura)
float_02 = float(peso)
print(f'{nome}, seu IMC é: {float_02 / (float_01 * float_01):.2f}', end='\n\n')






      




