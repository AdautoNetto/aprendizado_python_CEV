import moeda

p = float(input('Digite um valor: R$'))

print(f'O dobro de {p} é: {moeda.dobro(p) }')
print('-' *30)
print(f'A metade de {p} é: {moeda.metade(p)}')
print('-' *30)
print(f'O {p} aumentado em 13% é: {moeda.aumentar(p, 10)}')
print('-' *30)
print(f'O {p} diminuido em 10% é: {moeda.diminuir(p, 13)}')
print('-' *30)

