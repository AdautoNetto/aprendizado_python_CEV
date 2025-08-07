import moeda

p = float(input('Digite um valor: R$'))

print(f'O dobro de {moeda.moeda(p)} é: {moeda.dobro(p, True)}')
print('-' *40)
print(f'A metade de {moeda.moeda(p)} é: {moeda.metade(p, True)}')
print('-' *40)
print(f'aumentado em 13% é: {moeda.aumentar(p, 10, True)}')
print('-' *40)
print(f'diminuido em 10% é: {moeda.diminuir(p, 13, True)}')
print('-' *40)

