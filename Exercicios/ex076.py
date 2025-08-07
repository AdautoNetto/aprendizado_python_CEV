listagem = ('Lápis', 1.75,
            'Borracha', 2.50,
            'caderno', 21,
            'Agenda', 15,
            'Mochila', 115.99,
            'Estojo', 25,
            'Caneta', 2.50)
print('-'*40)
print(f'{"Lista de Produtos":^40}')
print('-' *40)
for produto in range(0, len(listagem)):
    if produto % 2 == 0:
        print(f'{listagem[produto]:.<30}', end='')
    else:
        print(f'R$ {listagem[produto]:.2f}')