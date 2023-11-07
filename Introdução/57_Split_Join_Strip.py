"""
SPLIT() -> Divide uma string através de um separador (espaço, ponto, vírgula...) e cria uma lista;
JOIN() -> Une uma string através de um separador informado fora de uma lista;
STRIP() -> Tira os espaços de uma string tanto da Esquerda quando Direita;
LSTRIP() -> Tira os espaços de uma string da Esquerda (Left);
RSTRIP() -> Tira os espaços de uma string da Direita (Right).

"""

phrase = 'Estou passando mal do estômago, não sei o que fazer!'

### SPLIT

phrase_croped = phrase.split() # Se nada for informado, será retornado uma lista separada por espaços vazios
print(phrase_croped) # ['Estou', 'passando', 'mal', 'do', 'estômago,', 'não', 'sei', 'o', 'que', 'fazer!']

phrase_croped = phrase.split(', ') # Separando por vírgula + espaço
print(phrase_croped) # ['Estou passando mal do estômago', 'não sei o que fazer!']


### STRIP
phrase_whitespace = '    Estou passando mal do estômago,     não sei o que fazer!    '
print(phrase_whitespace) #     Estou passando mal do estômago,     não sei o que fazer! 

phrase_whitespace_split = phrase_whitespace.split(',') # Separando por vírgula

phrase_correct = [] # Criando uma lista vazia para utilizar o 'append' dentro do FOR/IN:

for i, phrase in enumerate(phrase_whitespace_split):
    print(phrase.strip())   # Estou passando mal do estômago
                            # não sei o que fazer!
    phrase_correct.append(phrase_whitespace_split[i].strip())

print(phrase_correct) # ['Estou passando mal do estômago', 'não sei o que fazer!']


### JOIN
phrase_join = ', '.join(phrase_correct)
print(phrase_join) # Estou passando mal do estômago, não sei o que fazer!

abc_join = ' - '.join('abc') # Separa a string com Espaço + Hífen + Espaço
print(abc_join) # a - b - c 


