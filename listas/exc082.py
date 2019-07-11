par = []
impar = []
num = []

while True:
    n = int(input('Digite um número: '))
    num.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    op = input('Quer continuar? [S/N]')
    if op in 'nN':
        break
print(f'Lista completa: {num}')
print(f'Lista de pares: {par}')
print(f'Lista de ímpares: {impar}')
