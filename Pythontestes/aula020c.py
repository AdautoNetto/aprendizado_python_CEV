def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


lista = [4, 5, 6, 7, 2, 3]

dobra(lista)
print(lista)
