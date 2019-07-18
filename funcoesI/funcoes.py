def soma(a, b):
    s = a + b
    print(f'{a} + {b} = {s}')


soma(4, 5)
soma(8, 1)
soma(2, 1)


def contador(*num):
    tam = len(num)
    print()
    for v in num:
        print(f'{v} {tam}', end=' ')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 6, 7, 2)

valores = [7, 2, 5, 0, 4]


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


print()
dobra(valores)
print(valores)
