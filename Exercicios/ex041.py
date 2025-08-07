n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
m = (n1 + n2) / 2

if m < 5.0:
    print('REPROVADO')
elif m >= 5.0 and m < 7.0:
    print('Voce está de recuperação')
else:
    print('APROVADO')
