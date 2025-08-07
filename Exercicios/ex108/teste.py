import moeda

p = float(input('Digite um valor: R$'))

print(f'O dobro de {moeda.moeda(p)} é: {moeda.moeda(moeda.dobro(p))}')
print('-' *30)
print(f'A metade de {moeda.moeda(p)} é: {moeda.moeda(moeda.metade(p))}')
print('-' *30)
print(f'O {moeda.moeda(p)} aumentado em 13% é: {moeda.moeda(moeda.aumentar(p, 10))}')
print('-' *30)
print(f'O {moeda.moeda(p)} diminuido em 10% é: {moeda.moeda(moeda.diminuir(p, 13))}')
print('-' *30)

