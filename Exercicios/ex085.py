numeros = [[], []]

for c in range(0,7):
    numero = (int(input(f'Digite o {c+1} valor: ')))
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)
numeros[0].sort()
print(f'Os valores pares são: {numeros[0]}')
numeros[1].sort()
print(f'Os valores impares são: {numeros[1]}')
