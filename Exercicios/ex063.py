termo = int(input('Quantos termos voce quer mostar: '))
pt = 0
st = 1
print('{} -> {} -> '.format(pt, st), end='')
cont = 3
while cont <= termo:
    tt = pt + st
    print('{} -> '.format(tt), end='')
    pt = st
    st = tt
    cont += 1
print('FIM')
