cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete','oito', 'nove','dez',
          'onze', 'doze', 'treze', 'quatoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
          'dezenove', 'vinte')
escolha = 'S'

#enquanto a variavel escolha for S roda o programa
while escolha == 'S':
#pede a entrada d o usuario
    numero = int(input('Digite um numero: '))
#confere se o numero escolhido pelo usuario está entre 0 a 20
    if numero >= 0 and numero <= 20:
#mostra o numero por escrito para o usuario
        print(f'{cont[numero]}')
    else:
        while numero < 0 or numero > 20:
            print('voce digitou o numero invalido, tente novamente. ')
            numero = int(input('Digite um numero: '))

#enquanto infinito, irá parar só com o break
    while True:
#entrada do usuario
        escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
#verifica qual opção o usuario escolheu
        if escolha == 'N':
            print('Programa encerrado...')
            break
        elif escolha == 'S':
            break
        else:
            print('voce digitou uma opção inválida, tente novamente: ')
