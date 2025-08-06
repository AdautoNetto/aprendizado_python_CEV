try:
    a = int(input('digite um numero: '))
    b = int(input('digite um numero: '))
    r = a / b

except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__} ')

else:
    print(f'O resultado é: {r}')

finally:
    print('Volte sempre')
