import os
os.system('clear')
numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro')

while True:
    n = int(input('Digite um número de zero a quatro: '))
    if n >= 0 and n <= 4:  # 0 <= n <= 4
        print('Você digitou o número', (numeros[n]))
        break
    else:
        print("De 0 a 4")
