valores = []
#para adicionar valores a minha lista
valores.append(5)
valores.append(9)
valores.append(4)
print(f'A minha lista depois de adicionar os elementos(5, 9, 4): {valores}')
for v in valores:
   print(f'{v}...', end='')
#para mostra o elemento e o indice uso o enumerate
for c, v in enumerate(valores):
    print(f'\nNa posição {c} encotrei o valor: {v}')
print('Cheguei ao final da lista...')