print('-=' *24)
n = int(input('Escreva o numero que voce deseja saber a tabuada: '))
print('-=' *24)

print('-=' *7)
print('Tabuada do {}' .format(n))
print('-=' *7)

for c in range(0, 11):
   r = n * c
   print('{} x {} = {}'.format(n, c, r))