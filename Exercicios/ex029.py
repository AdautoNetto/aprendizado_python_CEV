vc = float(input('Qual foi a velocidade do carro: '))
if vc <= 80:
    print('Voce está na velocidade correta')
else:
    multa = 150 + (vc - 80) * 7
    print('Voce foi multado em R$150,00 e a cada KM a mais terá um custo adicional de R$7,00')
    print('No total voce irá pagar: R$ {:.2f}' .format(multa))
