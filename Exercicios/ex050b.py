p = 0
for c in range(0, 6):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
      p += n
print('As soma dos numeros pares são: {}'.format(p))