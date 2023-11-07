# EXERCICIOS

nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')
print('\n')

if nome and idade:
    print(f'Seu nome é:  {nome}', end='\n')
    print(f'Seu nome invertido é:  {nome[::-1]}', end='\n')
    # Não precisa especificar o que, pois toda informação no if é verdadeira, 
    # se estiver vazio é falso

    if ' ' in nome:
        print('Seu nome contém espaço(s). ', end='\n')
    else:
        print('Seu nome NÃO contém espaço(s).', end='\n')    
    print(f'Seu nome contém, {len(nome)} caractéres.', end='\n')
    print(f'A primeira letra do seu nome é:  {nome[0]}', end='\n')
    print(f'A última letra do seu nome é:  {nome[-1]}', end='\n\n')
else:
    print('Desculpe, você deixou campos vazios.', end='\n\n')

