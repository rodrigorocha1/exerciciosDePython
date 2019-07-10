import os
os.system('clear')
produtos = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90)

for produto in range(0, len(produtos)):
    if produto % 2 == 0:
        print(f'{produtos[produto]:.<10}')
    else:
        print(f'{produtos[produto]:.>10}')
