import time

o = 0

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

while o != 5:
    print('''[1] Somar 
[2] Multiplicar 
[3] Maior
[4] Novos Números 
[5] Sair do programa''')
    o = int(input('Qual é a sua opção: '))
    if o == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif o == 2:
        multiplicacao = n1 * n2
        print('A multiplicação entre {} e {} é: {}'.format(n1, n2, multiplicacao))
    elif o == 3:
        if n1 > n2:
            maior = n1
            print('O maior numero entre {} e {} é {} '.format(n1, n2, maior))
        elif n1 < n2:
            maior = n2
            print('O maior numero entre {} e {} é {} '.format(n1, n2, maior))
        else:
            print('Os numeros escolhidos são iguais ')
    elif o == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif o == 5:
        print('Saindo do programa...')
        time.sleep(2)
        print('Fim do programa!')
    elif o != 1 or o != 2 or o != 3 or o != 4 or o != 5:
        print('Voce digitou uma opção inválida. digite novamente.')
