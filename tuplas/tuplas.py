import os
os.system('clear')
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
# Tuplas são imutáveis
# lanche[1] = 'Refrigerante'
print(lanche)
print(lanche[-3:])

for comida in lanche:
    print('Eu vou comer %s na posição ' % comida)

for cont in range(0, len(lanche)):
    print(lanche[cont], cont)


for pos, comida in enumerate(lanche):
    print('Comida: %s -> Posição %d' % (comida,  pos))
print(sorted(lanche))  # tupla em ordem
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a
print(c)
print(d)
print(len(c))
print(c.count(c))
print('pos %d' % c.index(8))
pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)
