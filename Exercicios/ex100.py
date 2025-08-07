from random import randint
from time import sleep


#função para sortear valores
def sorteados(numeros):
    cont = 0
    print(f'Sorteando 5 valores da lista', end=' ')
    for cont in range (0, 5):
        cont += 1
        numeros.append(randint(0, 10,))
    for n in numeros:
        print(n, end = ' ', flush = True)
        sleep(0.3)
    print('PRONTO')


#funçaõ para somar os pares
def pares(numeros):
    print(f' A soma dos valores pares de {numeros} são:')
    p = 0
    for n in numeros:
        if n % 2 == 0:
            p += n
    print(f'{p}', end = ' ')


#programa principal
numeros = list()

sorteados(numeros)

pares(numeros)
