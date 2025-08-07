n = int(input('Digite um numero: '))

de = 0

for c in range(2, n):
    if n % c == 0:
        de += 1
if de == 0:
    print('Esse numero é PRIMO')
else:
    print('Esse numero NÃO é PRIMO')

