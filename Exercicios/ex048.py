print('Numeros impares divisiveis por 3 de 01 até 500')

nis = 0
for c in range(1, 500):
    if c % 3 == 0:
        print(c)
        print('-')
        nis += c

print('A soma de todos esses numeros é: {}'.format(nis))
