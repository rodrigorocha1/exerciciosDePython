import os
os.system('clear')
numeros = []

for num in range(0, 5):
    numeros.append(int(input('Digite número: ')))
print('Você digitou os valores: ', numeros)
pos_maior = []
pos_menor = []
for posicao, numero in enumerate(numeros):
    if numero == max(numeros):
        pos_maior.append(posicao)
    if numero == min(numeros):
        pos_menor.append(posicao)
print(f'O maior valor da lista é {max(numeros)}, nas posições {pos_maior}')
print(f'O maior valor da lista é {min(numeros)}, nas posições {pos_menor}')
print()
