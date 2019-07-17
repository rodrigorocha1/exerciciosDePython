from random import sample

jogos = []

qtd_jogos = int(input('Quantos jogos? '))
print('=' * 20, f'Sorteando {qtd_jogos} jogos', '=' * 20)
for c in range(qtd_jogos):
    a = sorted(sample(range(1, 61), 6))
    jogos.append(a[:])
    print(f'Jogos {c + 1}:{a}')
print('=' * 59)
