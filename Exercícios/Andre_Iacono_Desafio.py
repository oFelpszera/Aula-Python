"""from collections import Counter

fruit_list = ['Maçã', 'Morango', 'Maçã', 'Maçã', 'Banana', 'Abacate', 'Morango']

print('Minha lista de frutas é: ', fruit_list, '\n')

count = Counter(fruit_list)
visited = set()

for fruit in fruit_list:
    if fruit not in visited:
        print(f'{fruit} apareceu {count[fruit]}x.')
        visited.add(fruit)
print(fruit_list.count('Maçã'))"""



"""from termcolor import colored

fruit_list = [
    'Maçã', 'Morango', 'Maçã', 'Maçã', 'Banana', 'Abacate', 'Morango'
    ]

for i in set(fruit_list): 
    print(colored(f'A fruta {i} apareceu:', 'blue'),
          colored(f'{str(fruit_list.count(i))}x', 'yellow'))
print('\n')"""


from termcolor import colored

fruit_list = [
    'Maçã', 'Morango', 'Maçã', 'Maçã', 'Banana', 'Abacate', 'Morango'
    ]

for i in set(fruit_list): 
    print(colored('A fruta', 'blue'),
          colored(i, 'yellow'),
          colored('apareceu:', 'blue'),                  
          colored(f'{str(fruit_list.count(i))}x', 'yellow'))
print('\n')

