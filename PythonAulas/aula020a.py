def soma(a, b):
    print(f'A = {a}')
    print(f'B = {b}')
    s = a + b
    print(f'A soma entre {a} e {b} é {s}')


def sub(a, b):
    print(f'A = {a}')
    print(f'B = {b}')
    s = a - b
    print(f'A subtração entre {a} e {b} é {s}')


def div(a, b):
    print(f'A = {a}')
    print(f'B = {b}')
    s = a / b
    print(f'A divisão entre {a} e {b} é {s}')


def multi(a, b):
    print(f'A = {a}')
    print(f'B = {b}')
    s = a * b
    print(f'A multiplicação entre {a} e {b} é {s}')


#progama principal
n1 = int(input('Digite o primeiro numero que voce quer somar: '))
n2 = int(input('Digite o segundo numero que voce quer somar: '))
operação = str(input('Digite qual operação voce deseja fazer [+, -, /, x: '))
if operação == '+':
    soma(n1, n2)
elif operação == '-':
    sub(n1, n2)
elif operação =='/':
    div(n1, n2)
elif operação == 'x':
    multi(n1, n2)
else:
    print('Por favor digite uma operação válida...')