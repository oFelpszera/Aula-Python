# CONDIÇÕES COM "IF" = SE   //   "ELIF" = SE NÃO SE   //    "ELSE" = SE NÃO
# Podemos usar o "if" sozinho, mas o "elif" e "else" não, pois dependem do "if"


pergunta = input('Olá, Tudo bem? ("Sim" ou "Não") ')

if pergunta == 'Sim': # Dois pontos é o "então" - se tal coisa, então tal coisa.
    print('Que bom, fico feliz.', end='\n\n')
elif pergunta == 'Não': # Se não for a resposta de "if", se "elif", :"então"
    print('Então não posso fazer nada.', end='\n\n')
else: # Se não for a resposta de "if" ou "elif", então "else"
    print('Você não digitou uma resposta válida.', end='\n\n')
    print('Vamos tentar de novo.', end='\n')
    
