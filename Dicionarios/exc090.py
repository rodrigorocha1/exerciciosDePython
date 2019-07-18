alunos = dict()
alunos['nome'] = str(input('Nome: '))
alunos['media'] = float(input(f'Média de {alunos["nome"]}: '))

if 7 <= alunos["media"] <= 10:
    alunos["situacao"] = 'Aprovado'
elif 5 <= alunos["media"] <= 6.9:
    alunos["situacao"] = 'Recuperação'
else:
    alunos["situacao"] = 'Reprovado'

print(alunos)
print(f'- nome é igual a {alunos["nome"]}')
print(f'- média é igual a {alunos["media"]}')
print(f'- situacao {alunos["situacao"]}')
