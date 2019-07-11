pessoas = []
dados_pessoas = []
maior = menor = 0
while True:
    dados_pessoas.append(input('Nome: '))
    dados_pessoas.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados_pessoas[1]
    else:
        if dados_pessoas[1] > maior:
            maior = dados_pessoas[1]
        if dados_pessoas[1] < menor:
            menor = dados_pessoas[1]
    pessoas.append(dados_pessoas[:])
    dados_pessoas.clear()

    op = input('Quer continuar: [S/N] ? ').strip()
    if op in 'Nn':
        break
print(f'Pessoas: {len(pessoas)}')
print(f'Você cadastrou {len(pessoas)} pessoas')
print(f'Maior peso: {maior}. Pesos de ', end='')
for pessoa in pessoas:
    if pessoa[1] == maior:
        print(f'[{pessoa[0]}]', end='')
print()
print(f'Menor peso: {menor}. Pesos de ', end='')

for pessoa in pessoas:
    if pessoa[1] == menor:
        print(f'[{pessoa[0]}]', end='')
print()
