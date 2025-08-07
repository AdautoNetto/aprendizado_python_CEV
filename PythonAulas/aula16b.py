lanche = 'hamburguer', 'suco', 'pizza', 'pudim'
#quando eu não preciso mostrar a posição dos elementos, somente eles
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('-=' *15)
#quando eu preciso mostrar a posição e os elementos
for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}, na posição {cont}')
print('-=' *15)
#quando eu preciso mostrar a posição e os elementos
for posição, comida in enumerate(lanche):
    print(f'Eu vou comer {comida}, na posição {posição}')

print('Comi pra caramba')