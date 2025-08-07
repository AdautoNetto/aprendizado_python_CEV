print('----CALCULANDO PA----')
pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
termo = pt
c = 1
while c <= 10:
    print('{} -> '.format(termo), end='')
    termo += r
    c += 1
print('FIM')