jogador = dict()
totgols = 0

jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas o {jogador['nome']} jogou: '))
jogador['gols'] = list()

for g in range(0, partidas):
    jogador['gols'].append(int(input(f'Quantos gols na partida {g+1} o {jogador['nome']} fez: ')))
    totgols = sum(jogador['gols'])
jogador['total'] = totgols
print('-=' *30)
print(jogador)
print('-=' *30)
for k, v in jogador.items():
    print(f'o campo {k} tem valor {v}')
print('-=' *30)
print(f'O jogador {jogador['nome']} jogou {partidas} partidas')
for i, g in enumerate(jogador['gols']):
    print(f'Na partida {i + 1}, fez {g} gol')
print(f'Foi um total de {jogador['total']} gols em {partidas} partidas')