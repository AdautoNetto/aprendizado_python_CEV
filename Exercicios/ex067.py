n, c, r = 0, 0, 0

while True:
    print('TABUADA (Digite um numero negativo para parar o programa)')
    print('-' *37)
    n = int(input('Voce quer ver a tabuda de qual valor: '))
    print('-' * 37)
    if n < 0:
        print('O numero que voce digitou é negativo. encerrando o programa...')
        break
    c = 0
    while c < 11:
        r = n * c
        print(f'{n} x {c} = {r}')
        c += 1


