num = []

while True:
    num.append(int(input('Digite um número: ')))
    op = input('Quer continuar? [S/N] ')
    if op in 'Nn':
        break

print(f'Você digitou {len(num)} números')
num.sort(reverse=True)
print(f'Ordem decrescente {num}')
if 5 in num:
    print('O valor 5 faz parte da lista')

