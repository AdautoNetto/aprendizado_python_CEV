r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Essas retas podem formar um triangulo ')
    if r1 == r2 == r3:
        print('TRIANGULO EQUILATERO')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('TRIANGULO ISÓCELES')
    else:
        print('TRIANGULO ESCALENO')
else:
    print('Essas retas não podem formar um triangulo')
