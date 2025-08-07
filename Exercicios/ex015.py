d = int(input('Quantos dias voce ficou como o carro: '))
pd = d * 60
kmr = float(input('Quantos km voce andou com o carro: '))
pkm = kmr * 0.15
pt = pd + pkm
print('o valor que voce irá pagar pelos dias são de: R${:.2f}' .format(pd))
print('O valor que voce irá pagar pelo km rodados são de: R${:.2f}' .format(pkm))
print(f'E o valor total que voce irá pagar vai ser de: {pt:.2f}')