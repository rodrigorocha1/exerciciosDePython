import os
os.system('cls')


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = 5
print(f'O fatorial de {n} é igual a {fatorial(n)}')
