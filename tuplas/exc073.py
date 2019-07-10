import os
os.system('clear')

times = ('Palmeiras', 'Santos', 'Flamengo', 'Internacional', 'Atlético Mineiro', 'Goiás', 'Botafogo', 'Bahia', 'São Paulo',
         'Corinthians', 'Grêmio', 'Atlético Paranaense', 'Ceara', 'Fortaleza', 'Vasco', 'Fluminense', 'Chapecoense', 'Cruzeiro', 'CSA', 'Avaí')
print('Lista dos times do Brasileirão ', times)
# a) Os 5 primeiros times.
print('=-' * 20)
print('Os 5 primeiros times', times[0:5])
print('=-' * 20)
# b) Os últimos 4 colocados
print('Os quatro últimos', times[-4:])
print('=-' * 20)
# c) Times em ordem alfabética.
print('Times em ordem alfabetica', sorted(times))
print('=-' * 20)
# d) Em que posição está o time da Chapecoense.
print('Posição da chapecoense', times.index('Chapecoense') + 1)
