import random

print('----------------------')
print(' Vamos Jogar Jokenpô')
print('----------------------')
print('Vou fazer a minha escolha...')
op = int(input('Digite qual opção voce irá jogar: '
              ' \n[0] PEDRA'
              ' \n[1] PAPEL'
              ' \n[2] TESOURA'
              ' \nDigite a sua escolha: '))

oe = ('PEDRA', 'PAPEL', 'TESOURA')
computador = random.randint(0, 2)

if op == 0:
    op = ('PEDRA')
elif op == 1:
    op = ('PAPEL')
elif op == 2:
    op = ('TESOURA')
print('-=' *15)
print('COMPUTADOR escolheu {}' .format(oe[computador]))
print('-=' *15)
print('JOGADOR escolheu {}' .format(op))
print('-=' *15)

if op == computador:
    print('EMPATE')
elif op == 0 and computador == 1:
    print('VOCE PERDEU')
elif op == 0 and computador == 2:
    print('VOCE GANHOU')
elif op == 1 and computador == 0:
    print('VOCE GANHOU')
elif op == 1 and computador == 2:
    print('VOCE PERDEU')
elif op == 2 and computador == 0:
    print('VOCE PERDEU')
elif op == 2 and computador == 1:
    print('VOCE GANHOU')
elif op != 0 or 1 or 2:
    print('Voce escolheu uma opção inválida. TENTE NOVAMENTE')

print('TENTE NOVAMENTE')
