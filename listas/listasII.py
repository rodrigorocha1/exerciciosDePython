teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)
tot_mai = tot_men = 0
'''era = []
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

galera_2 = [['João', 19], ['Ana', 33], ['An3', 35] ,['An4', 34]]
print(galera[0][0])

for p in galera_2:
    print(p)
    print(p[0])
'''
galera = list()
dado = list()
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]}')
        tot_mai += 1
    else:
        print(f'{p[0]}')
        tot_men = 1
print(f'{tot_mai} -> {tot_men}')