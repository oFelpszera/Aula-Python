"""
FAÇA UM JOGO PARA O USUÁRIO ADIVINHAR QUAL A PALAVRA SECRETA.

- VOCÊ VAI PROPOR UMA PALAVRA SECRETA QUALQUER E VAI DAR A POSSIBILDADE PARA O USUÁRIO
DIGITAR APENAS UMA LETRA.

- APÓS A DIGITAÇÃO VOCÊ VAI CONFERIR SE A LETRA DIGITADA ESTÁ NA PALAVRA SECRETA.
- SE SIM, EXIBA A LETRA.
- SE NÃO, EXIBA ASTERISCO (*).

- FAÇA A CONTAGEM DE TENTATIVAS.

"""
import os
from termcolor import colored

secret_word = 'Oppenheimer'.upper()
letter = ''
rep = 0

while True:
    typed_letter = input('Digite uma letra: ').upper()

    # CONSULTA PARA SABER SE O USUÁRIO DIGITOU APENAS 1 LETRA:
    if len(typed_letter) == 1:

        ## CONULTA PARA SABER SE A LETRA DIGITADA CONTÉM NA PALAVRA SECRETA:           
        if typed_letter in secret_word:
            letter += typed_letter

            ### CRIANDO UM LOOPING PARA EXIBIR A LETRA DIGITADA NA POSIÇÃO CORRETA OU PREENCHER COM '*':
            secret_letter = ''
            for i in secret_word:                
                if i in letter:
                    secret_letter += i
                else:
                    secret_letter += '*'                    
            print(f'{secret_letter} \n')

            #### SE O USUÁRIO ACERTAR TODAS AS LETRAS:
            if secret_letter == secret_word:
                os.system('cls') # LIMPAR O TERMINAL
                print('\n')
                print('PARABÉNS! VOCÊ DESCOBRIU A PALAVRA SECRETA!')
                print(colored(f'{secret_word}', 'blue')) # COR AZUL
                print(f'Você errou um total de: {rep}x. \n')

            #### QUESTIONAR SE O USUÁRIO DESEJA CONTINUAR JOGANDO:                
                keep_playing = input('Deseja Continuar? [S] [N]: ').upper()

            #### SE SIM:
                if keep_playing.startswith('S'):
                    print('Vamos Iniciar! \n')
                    # LIMPA OS DADOS ANTERIORES:
                    secret_word = 'Transformers'.upper()
                    letter = ''
                    rep = 0
            #### SE NÃO:

                elif keep_playing.startswith('N'):
                    print('Ok! Jogo Finalizado! \n')
                    break

            #### SE NADA FOR DIGITADO:
                else:
                    print('Letra Inválida, GAME OVER! \n')
                    break

        ## SE O USUÁRIO DIGITAR LETRA QUE NÃO EXISTE:           
        else: 
            print('Letra não existe! \n')
            rep += 1

    # SE O USUÁRIO DIGITAR MAIS DE UMA LETRA:
    else:
        print('Digite apenas uma letra. \n')
        rep += 1


        

            


