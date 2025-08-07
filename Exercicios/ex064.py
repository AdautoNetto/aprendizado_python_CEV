cont = 0
resultado = 0


numero = int(input('Digite um numero: '))

while numero != 999:
    resultado += numero
    cont += 1
    numero = int(input('Digite um numero: '))

print('A soma dos numeros é: {}'.format(resultado))
print('Voce digitou {} numeros ' .format(cont))
