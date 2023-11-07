"""
CONSTANTE = "Variaveis" que não vão mudar.
Para indicar a outros programadores, ou eu mesmo no futuro, que uma variavel não irá mudar
escrevemos ela com letra MAIUSCULA.
- O que é ruim em um código?
1. Muitas condições no mesmo "if", muitas linhas, muito espaço para iniciar o código.
- O que é bom em um código?
1. Deixar a linguagem limpa. De um modo que quem ler, endetenderá só de olhar.
"""

velocidade_carro = 101 # Velocidade Atual do Carro
local_carro = 100 # Km 100 de uma rodovia

RADAR_01 = 100 # CONSTANTE que não irá mudar, representa a velocidade max. do Radar 1
LOCAL_RADAR = 100 # Km onde o Radar 1 está na rodovia
RADAR_RANGE = 1 # Campo onde o Radar 1 irá multar 1km a mais e a menos (99 - 100 - 101)

if local_carro >= (LOCAL_RADAR - RADAR_RANGE) and \
    local_carro <= (LOCAL_RADAR + RADAR_RANGE): # Barra invertida representa a quebra de linha
    print('Carro Passou no Radar 01')
if velocidade_carro > RADAR_01:
    print('Carro Acima da Velocidade no Radar 01. ')
if velocidade_carro > RADAR_01 and local_carro >= (LOCAL_RADAR - RADAR_RANGE) and \
    local_carro <= (LOCAL_RADAR + RADAR_RANGE):
    print('Carro Multado.', end='\n\n')
    print('-' * 15, end='\n\n') # Retonar 15 hífens

# Porém o código está muito grande, cheio de linhas e condições.
# Podemos criar variáveis para as condições.

local_carro_antes = local_carro <= (RADAR_01 + RADAR_RANGE)
local_carro_depois = local_carro >= (RADAR_01 - RADAR_RANGE)
multa = velocidade_carro > RADAR_01

carro_passou_no_radar = local_carro_antes and local_carro_depois
carro_multado = carro_passou_no_radar and multa

if carro_passou_no_radar:
    print('Carro Passou no Radar 01')
else:
    print('Carro fora do Radar 01.')
if multa:
    print('Carro Acima da Velocidade no Radar 01. ')
if carro_multado:
    print('Carro Multado.', end='\n\n')

