numeros = [[], []]

for i in range(0, 7):
    num = int(input(f'Digite {i + 1}º número: '))
    if num % 2 == 0:
        numeros[1].append(num)
    else:
        numeros[0].append(num)
print(f'Valores pares {numeros[0]}')
print(f'Valores ímpares {numeros[1]}')
