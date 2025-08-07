import random

numero = int(input('Tente acertar qual numero eu vou escolher... (de 0 a 5): '))

lista = [0, 1, 2, 3, 4, 5]

ne = random.choice(lista)

if numero == ne:
     print('O numero escolhido foi: {}, e o que voce escolheu foi: {}'.format(ne, numero))
     print('Voce acertou!!!')
else:
    print('O numero escolhido foi: {}'.format(ne))
    print('Voce perdeu...')
print('Teste a sua sorte novamente')