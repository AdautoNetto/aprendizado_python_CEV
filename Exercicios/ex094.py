pessoa = dict()
pessoas = list()
escolha = 'S'
soma_idade = 0

while escolha == 'S':
    pessoa['nome'] = str(input('nome: '))
    while True:
        pessoa['sexo'] = str(input('sexo: [M|F]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        else:
            print('ERRO ! por favor digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma_idade += pessoa['idade']
    pessoas.append(pessoa.copy())
    pessoa.clear()
    while True:
        escolha = str(input('Quer continuar [S|N]: ')).strip().upper()[0]
        if escolha == 'N':
            print('encerrando o programa...')
            break
        elif escolha == 'S':
            break
        else:
            print('ERRO ! responda apenas S ou N')
print('-=' *30)
print(f' A) Foram cadastradas {len(pessoas)} pessoas')
media = (soma_idade / len(pessoas))
print(f' B) A média de idade é de {media: .2f} anos')
print('\nC) As mulheres cadastradas foram: ', end = ' ')
for m in pessoas:
    if m['sexo'] == 'F':
        print(m['nome'], end = ' ')
print(' D) A lista de pessoas acima da média de idade: ')
for p in pessoas:
    if p['idade'] > media:
        print(f'{p}')
