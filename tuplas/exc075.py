import os
os.system('clear')

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))
valores = (n1, n2, n3, n4)
print('Você digitou os valores', valores)
print('O número 9 apareceu  vezes', (valores.count(9)))
print('O valor 3 apareceu na  posição', (valores.index(3)))
print('Os valores pares digitados foram', end=' ')
for valor in valores:
    if valor % 2 == 0:
        print(valor, end='\n')
