aluno = dict()

nome = str(input('Nome: '))
media = float(input(f'Média de {nome} é: '))

if media >= 6:
    aluno['situacao'] = 'aprovado'
else:
    aluno['situacao'] = 'reprovado'
print(f'A média de {nome} é: {media}')
print(f'{nome} está', end =' ')
for s in aluno.values():
    print(s)
