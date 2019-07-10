import os
os.system('clear')
numeros = []

while True:
    n = int(input('Digite um número: '))
    if n in numeros:
        print(f'O número {n} está na lista')
    else:
        numeros.append(n)
    op = input('Quer continuar? [S/N] ')
    if op in 'Nn':
        break
print(numeros)
