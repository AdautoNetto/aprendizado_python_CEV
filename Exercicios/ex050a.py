n = int(input('Digite até que numero voce quer somar: '))

s = 0
for c in range(1, n):
    if c % 2 == 0:
        print(c)
        s += c
print('A soma dos numeros pares é: {}' .format(s))
