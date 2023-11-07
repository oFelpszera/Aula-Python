# EXERCÍCIO CÁLCULO IMC
# O IMC -> Divide o peso (em kg) pela altura ao quadrado (em m)

nome = 'Felipe Andrade'
peso = 78.65
altura = 1.80
imc_01 = peso / (altura ** 2)
imc_02 = peso / (altura * altura)

print(nome, 'tem', altura, 'de altura', end=',\n')
print('pesa', peso, 'quilos e seu IMC é', end=':\n')
print(imc_01)
print(imc_02, end='\n\n')

imc = ... 
# Os três pontos "..." são chamados de Ellipses, sua função é informar que o
# código ainda não foi escrito, ele não gera erro, serve como um "Place Holder"

