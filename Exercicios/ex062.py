print('----CALCULANDO PA----')
pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
termo = pt
c = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while c <= total:
        print('{} -> '.format(termo), end='')
        termo += r
        c += 1
    print('PAUSA')
    mais = int(input('Voce quer mostrar mais algum termo: '))
print('O programa chegou ao fim com {} termos.'.format(total))