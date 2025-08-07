numero = (input('Digite um numero inteiro: '))

numero = numero.zfill(4)

print('Unidade {}' .format(numero[3]))
print('Dezena {}' .format(numero[2]))
print('Centena {}' .format(numero[1]))
print('Milhar {}' .format(numero[0]))