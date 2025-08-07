times = ('Atlético Mineiro', 'Bahia', 'Botafogo', 'Ceará', 'Corinthians', 'Cruzeiro', 'Flamengo',
         'Fluminense', 'Fortaleza', 'Grêmio', 'Internacional', 'Juventude', 'Mirassol', 'Palmeiras',
         'Red Bull Bragantino', 'Santos', 'São Paulo', 'Sport Recife', 'Vasco da Gama', 'Vitória')
cont = 0

print('-=' *33)
print(f'os 5 primeiros times são: {times[:5]}')
print('-=' *33)
print(f'os quatros ultimos times são: {times[-4:]}')
print('-=' *33)
print(f'Os times em ordem alfabéticas: {sorted(times)}')
print('-=' *33)
print(f'O São Paulo está na {times.index('São Paulo') +1} posição ')
#laço de repetição para saber qual time está na ultima posição
while True:
    cont += 1
    if cont == 19:
        print('-=' *33)
        print(f'na ultima posição está o: {times[cont]}')
        print('-=' *33)
        break
time_escolhido = str(input('Digite o nome do time que voce deseja saber a posição: '))
if time_escolhido in times:
    print(f'O {time_escolhido} está na {times.index(time_escolhido) +1} posição')
else:
    print('Voce digitou o nome do time errado')