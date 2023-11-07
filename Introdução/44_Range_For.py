# RANGE é uma CLASSE onde você define o tamanho da informação, através do inicio, fim e passos:
# RANGE(star, stop, step) -> o STOP é obrigatorio, se tiver apenas um valor, ele será STOP, o START será '0 e o STEP será '1'.

numeros = range(0, 11) # 0 à 10 o último número não considera
tabuadas = range(1, 6) # 0 à 5 o último número não considera

for tabuada in tabuadas:
    for numero in numeros:
        resultado = tabuada * numero
        print(f'{tabuada} * {numero} = {resultado}')
    print('\n')