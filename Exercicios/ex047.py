n = int(input('Escolha até qual numero voce quer: '))
print('Mostrando os numeros pares entre 0 a {}' .format(n))
if n % 2 == 0 :
    for c in range(2, n +2):
        if c % 2 == 0:
            print(c)
        else:
            print('--')
elif n % 2 != 0 :
    for c in range(2, n):
        if c % 2 == 0:
            print(c)
        else:
            print('--')
