d = float(input('Qual a distancia da sua viagem em KM: '))
if d <= 200 :
    p = d * 0.50
    print('A sua viagem irá custar: R$ {:.2f}' .format(p))
else :
    p = d * 0.45
    print('A sua viagem irá custar: R$ {:.2f}' .format(p))
