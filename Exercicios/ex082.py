pares, impares, numeros = [], [], []
escolha = 'S'

#laço de repetição que vai se acabar quando o usuario digita 'S'
while escolha == 'S':
#variavel simples que vai guardar o numero digitado do usuario
        numero =(int(input('Digite um valor: ')))
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
#comando que vai pear o numero digitado pelo usuario e colocar na lista
        numeros.append(numero)
#laço de repetição infinito que para quando o usuario digitar 'S' ou 'N'
        while True:
            escolha = str(input('Voce quer continuar [S|N]: ')).strip().upper()[0]
# se dentro da variavel escolha tiver a letra 'S' ou 'N' termina esse laço
            if escolha in 'SN':
                break
# se dentro da variavel escolha não tiver a letra 'N' ou 'S' continua o laço
            else:
                continue
print(f'A lista completa é {numeros}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
