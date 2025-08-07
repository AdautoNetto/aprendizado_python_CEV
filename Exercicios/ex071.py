ced50 = 0
ced20 = 0
ced10 = 0
ced1 = 0

print('-=' *20)
print('         CAIXA ELETRONICO')
print('-=' *20)

valor = int(input('Digite o valor que irá ser sacado: R$'))
total = valor

while True:
    if total >= 50:
        ced50 += 1
        total -= 50
    elif total >= 20:
        ced20 += 1
        total -= 20
    elif total >= 10:
        ced10 += 1
        total -= 10
    elif total >= 1:
        ced1 += 1
        total -= 1
    else:
        break
print('-=' *20)
print(f'voce irá sacar R$ {valor:.2f}')
print(f'voce irá sacar {ced50} cédula(s) de 50 reais')
print(f'voce irá sacar {ced20} cédula(s) de 20 reais')
print(f'voce irá sacar {ced10} cédula(s) de 10 reais')
print(f'voce irá sacar {ced1} cédula(s) de 1 real')