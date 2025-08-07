from random import randint
import time
from operator import itemgetter

jogadas = {}
ranking = dict()

for c in range(0, 4):
   c += 1
   print(f'O {c}° jogador tirou ', end = '')
   time.sleep(1)
   jogadas[f'jogador{c}'] = randint(0, 6)
   print(f'{jogadas[f'jogador{c}']} no dado')
   time.sleep(1)
print('Ranking dos jogadores')
c = 0

ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)

for k, v in enumerate(ranking):
   c += 1
   print(f'{c} lugar: com {v[0]} com {v[1]}')
   time.sleep(1)
