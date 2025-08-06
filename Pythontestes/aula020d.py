def soma(*num):
    s = 0
    for n in num:
        s += n
    print(f'Somandos os valores {num} ficou: {s}')


soma(2, 5, 9, 2)
soma(9, 3, 6, 0, 7)