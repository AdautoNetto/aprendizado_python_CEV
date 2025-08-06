import collections
from itertools import count

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
#metodo para mostar quantas vezes um elemento aparece na varivel
print(f'o elemento 5 aparece {c.count(5)} vezes')
print('-=' *16)

#metodo para mostrar em qual posição o elemento aparece
print(f'o elemento 8 aparece na {c.index(8)} posição')
print('-=' *16)

# se um elemento aparece duas vezes ele vai mostrar a primeira aparição dele
print(f'o elemento 5 aparece na {c.index(5)} posição')
print('-=' *16)

#para mostrar a segunda aparição do elemento
print(f'a segunda aparição do elemento 5 é na {c.index(5, 2)} posição')
print('-=' *16)
