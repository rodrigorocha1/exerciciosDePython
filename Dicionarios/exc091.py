from random import randint
from time import sleep
from operator import itemgetter

resultado2 = {}
for i in range(0, 4):
    resultado2.update({f'jogador {i + 1}': randint(1, 6)})
print(resultado2)

print()
for n, l in resultado2.items():
    print(f'{n} tirou {l} no dado')
    sleep(1)

print("*" * 10, 'Ranking dos jogadores', "*" * 10)
placar = sorted(resultado2.items(), key=itemgetter(1), reverse=True)
print(placar)
for i, p in enumerate(placar):
    print(f'{i + 1}º lugar: {p[0]} com {p[1]}')