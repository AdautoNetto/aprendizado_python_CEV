n1 = float(input('Digite a sua nota: '))
n2 = float(input('Digite a sua nota: '))
m = (n1 + n2) / 2
print('A sua média é: {:.1f}' .format(m))
if m >= 6.0:
    print('A sua média foi boa, parabéns !!!')
else:
    print('A sua Média foi ruim, estude mais...')