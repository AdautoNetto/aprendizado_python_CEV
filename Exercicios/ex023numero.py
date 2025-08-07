n = int(input('Digite o Numero: '))

unidade = n % 10
print('Unidade {}' .format(unidade))

dezena = n // 10 % 10
print('Dezena {}' .format(dezena))

centena = (n // 100) % 10
print('Centena {}' .format(centena))

milhar = (n // 1000) % 10
print('Milhar {}' .format(milhar))