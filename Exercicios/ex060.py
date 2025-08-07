# USANDO O LAÇO DE REPETIÇÃO WHILE
numero = int(input('Digite o número que voce deseja calcular o fatorial: '))
c = numero
f = 1
while c > 0:
    print(' {} ' .format(c), end='')
    print('x' if c > 1 else '=', end='')
    f *= c
    c -= 1
print('{}'.format(f), end='')

# USANDO O LAÇO DE REPETIÇÃO FOR

numero = int(input('Digite o numero que voce deseja calcular o fatorial: '))
c = numero
f = 1

for c in range(numero, 0, -1):
    print('{}'.format(c), end='')
    print('x' if c > 1 else '=', end='')
    f *= c
    c -= 1
print('{}'.format(f))
