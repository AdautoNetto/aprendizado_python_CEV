valores = list()
#para pedir a entrada do usuario e guardar em uma lista
for cont in range(0, 2):
    valores.append(int(input('Digite um valor: ')))
print(valores)
print('-=' *30)
#para mostrar cada valor e o indice do valor do usuario juntos
for valor in enumerate(valores):
    print(f'Primeiro aparece o indice e depois o valor digitado: {valor}')
    print('-' *60)
print('-=' *30)
#para mostrar cada valor e o indice do valor do usuario separados
for indice, valor in enumerate(valores):
    print(f'Primeiro aparece o indice {indice} e depois o valor digitado: {valor}')
    print('-' *60)
print('-=' *30)
#para mostrar somente o indice, sem o valor
for i in range(len(valores)):
    print(f'Indice de dentro da lista')
    print('-' *30)
print('-=' *30)
#para mostrar somente o valor, sem o indice
for v in valores:
    print(f'Valor digitado: {v}')
    print('-' *20)
print('-=' *30)