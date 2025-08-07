s = float(input('Digite o valor do seu salário: '))
if s <= 1250:
    p = (s * 15) / 100
    sa = s + p
else:
    p = (s * 10) / 100
    sa = s + p
print('O seu salário atual é de: R${:.2f}'.format(sa))
