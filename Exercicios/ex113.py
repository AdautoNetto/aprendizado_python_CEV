def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'ERRO: por favor digite um numero inteiro válido')
            continue
        except (KeyboardInterrupt):
            print('não houve entrada de dados do usuario')
        else:
            return n

def leiareal(msg):
    while True:
        try:
                n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor digite um numero real válido')
            continue
        else:
            return n


num = leiaint('Digite um numero inteiro: ')

nu = leiareal('Digite um numero real: ')

print(f' Os numeros digitado foi {num} e {nu}')

