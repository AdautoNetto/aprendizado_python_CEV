from math import hypot

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hipo = hypot(co, ca)
print('A hipotenusa do do seu triangulo retangulo é: {:.2f}' .format(hipo))