numeros = []
maior, menor = 0, 0
#laço de repetição FOR para o usuario digita o valor 5 vezes e salvar na lista numeros
for cont in range(0,5):
    numeros.append(int(input(f'Digite um valor na posição {cont+1}: ')))
#se for o primeiro numero digitado a variavel maior e menor recebe o primeiro numero
    if cont == 0:
        maior = menor = numeros[cont]
    else:
#para ler o número digitado pelo usuario e verificar se ele é maior que o anterior
        if numeros[cont] > maior:
            maior = numeros[cont]
#para ler o numero digitado pelo usuario e verificar se ele é menor que o anterior
        if numeros[cont] < menor:
            menor = numeros[cont]
#mostrar os numeros digitados
print(f'Os numeros digitados foram: {numeros}')
#mostrar o maior numero digitad
print(f'O maior numero digitado foi: {maior}, nas posições:', end=' ')
#laço de repetição FOR para ler o numeros e os indices de cada numero de dentro da lista
for i, v in enumerate(numeros):
#se o valor digitado for igual o maior mostrar o indice dele
    if v == maior:
        print(f'{i+1}...', end='')
#mostrar o menor numero
print(f'\nO menor numero digitado foi: {menor}, nas posições: ', end=' ')
#laço de repetição FOR para ler os numeros e os indices de cada numero de dentro da lista
for i, v in enumerate(numeros):
#se o valor digitado for igual o menor numero mostrar o indice dele
    if v == menor:
        print(f'{i+1}...', end=' ')