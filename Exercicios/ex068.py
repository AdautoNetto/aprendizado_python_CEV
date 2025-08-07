# importação da biblioteca para o computador escolher um numero
import random

#variveis
numero, computador, soma, vitorias = 0, 0, 0, 0
pi = ''
while True:
    print('='*25)
    print('Vamos jogar PAR ou IMPAR')
    print('='*25)
#pegar a jogada do usuario
    numero = int(input('Digite a sua jogada: '))
    pi = str(input('Voce quer ser par ou impar[P|I]: ')).upper()[0]
#jogada do computador
    computador = random.randint(1, 10)
    print(f'a sua jogada foi {numero} e a jogada do computador foi {computador}')
#somar dos dois numeros mais o resto da divisão por dois para verificar se o numero é par
    s = (numero + computador) % 2
# condição se o jogador escolher PAR
    if pi == 'P':
        if s == 0:
            print('Deu PAR')
            print('parabéns voce ganhou !!!')
            print('Vamos jogar novamente...')
            vitorias += 1
        else:
            print('Deu IMPAR')
            break
#Condição se o jogador escolher IMPAR
    if pi == 'I':
        if s == 1:
            print('Deu IMPAR')
            print('parabéns voce ganhou !!!')
            print('Vamos jogar novamente...')
            vitorias += 1
        else:
            print('Deu PAR')
            break
print(f'GAME OVER. Voce venceu {vitorias} vezes')