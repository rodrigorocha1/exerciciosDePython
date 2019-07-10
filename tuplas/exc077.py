import os
os.system('clear')
palavras = ('AVIÃO', 'CARRO', 'FUTEBOL')
for palavra in palavras:
    print('Na palavra ' + palavra + ' temos as vogais ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiouã':
            print(letra.lower(), end=' ')
    print()
