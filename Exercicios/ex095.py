import copy

jogador = dict()
time = list()
totgols = 0
dados = 0

while True:
    jogador['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas o {jogador['nome']} jogou: '))
    jogador['gols'] = list()
    for g in range(0, partidas):
        jogador['gols'].append(int(input(f'Quantos gols na partida {g+1} o {jogador['nome']} fez: ')))
        totgols = sum(jogador['gols'])
    jogador['total'] = totgols
    time.append(copy.deepcopy(jogador))
    jogador.clear()
    while True:
        escolha = str(input('Voce quer continuar [S|N]: ')).strip().upper()[0]
        if escolha in 'SN':
            break
        else:
            print('tente novamente.')
    if escolha == 'N':
        break
print('-=' *30)
print(f'{"Cod":<5}{"Nome":<10}{"Gols":<15}{"Total":<10}')
print('-' *35)
for i, jogador in enumerate(time):
    print(f'{i:<5}{str(jogador["nome"]):<10}{str(jogador["gols"]):<15}{str(jogador["total"]):<10}')
while dados != 999:
    dados = int(input('Voce quer mostrar os dados de qual jogador (999 para parar): '))
    if dados == 999:
        print('Encerrando o programa...')
        break
    elif dados > len(time):
        print(f'Não existe jogador {dados}, por favor digite novamente ')
    else:
        for i, v in enumerate(time):
            if dados == i:
                print(f'-> LEVANTAMENTO DO JOGADOR {v["nome"]}')
                for p, g in enumerate(v['gols']):
                    print(f'Na partida {p + 1}, fez {g} gol')
