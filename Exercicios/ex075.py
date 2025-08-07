n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n3 = int(input('Digite mais um valor: '))
n4 = int(input('Digite o ultimo valor: '))

tupla = (n1, n2, n3, n4)
print('Voce digitou os valores: ', end='')

for cont in range (0, len(tupla)):
    print(f'{tupla[cont]}', end=' ')

if 9 in tupla:
    print(f'\nO valor 9 apareceu {tupla.count(9)} vezes')
else:
    print('\nO valor 9 não apareceu nenhuma vez...')

if 3 in tupla:
    print(f'o valor 3 apareceu na {tupla.index(3)+1} posição')
else:
    print(f'Voce não digitou o valor 3')

print(f'Os valores pares digitados foram: ', end='')
for p in tupla:
    if p % 2 == 0:
        print(p, end='  ')


