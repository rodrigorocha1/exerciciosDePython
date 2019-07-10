import os
os.system('clear')
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
num.remove(2)
if 5 in num:
    num.remove(5)
else:
    print('Não encontrei')
print(num)
print('Essa lista tem %d números' % len(num))

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
'''
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
'''
for c, valor in enumerate(valores):
    print('pos: %d -> valor: %d' % (c, valor))
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(a)
print(b)
