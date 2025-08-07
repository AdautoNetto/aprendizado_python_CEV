matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares, numeros, terceira_coluna, maior_segunda_linha = 0, 0, 0, 0
cont = 0
for l in range(0, 3):
    for c in range(0,3):
        numeros = int(input(f'Digite um valor para [{l}, {c}]: '))
        if l == 1:
            cont +=1
            if cont == 0:
                maior_segunda_linha = numeros
            if numeros > maior_segunda_linha:
                maior_segunda_linha = numeros
        if c == 2:
            terceira_coluna += numeros
        if numeros % 2 == 0:
            pares += numeros
        matriz[l][c] = numeros
print('-=' *30)
for l in range(0, 3):
    for c in range(0,3):
        print(f'[{matriz[l][c]: ^5}]', end = '')
    print()
print('-=' *30)
print(f'A soma dos numeros pares são: {pares}')
print(f'A soma dos valores da terceira coluna são: {terceira_coluna}')
print(f'O maior numeros da segunda linha é: {maior_segunda_linha}')
