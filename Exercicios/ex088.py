#importando bibliotecas que vou precisar usar
from random import randint
import time
#criando variaveis que vou precisar usar
jogos, cont, c, numero = 0, 0, 0, 0
jogo = list()
#menu
print('-=' *20)
print(f'          JOGA NA MEGA SENA')
print('-=' *20)
#pergunta ao usuario quantos jogos ele vai jogar e guarda a entrada dele
jogos = int(input('Quantos jogos voce quer jogar: '))
print(f'-----SORTEANDO {jogos} JOGOS-----')
#laço WHILE enquanto o contador for diferente da variavel jogos que é a entrada do usuario, roda
while cont != jogos:
    #zera a variavel que conta quantos numeros já foi
    c = 0
    #laço WHILE enquanto o contador(c) for menor que 6(qntd de numeros por jogo), roda
    while c < 6:
        #variavel numeros recebe um numero aleatório de 0 a 60
        numero = (randint(1, 60))
        #condição IF se numero aleatório não estiver na lista, adiciona ele
        if numero not in jogo:
            jogo.append(numero)
            # contador(c) recebe ele mesmo mais um toda vez que adicionar um numero na lista
            c += 1
    #organiza a lista final de forma crescente
    jogo.sort()
    #mostra a lista final
    print(f'{cont+1}°JOGO: {jogo}')
    #faz o usuario esperar 1 segundo
    time.sleep(1)
    #limpa a lista para mostrar outro jogo
    jogo.clear()
    #contador(cont) recebe ele mesmo mais um toda vez que eu jogo estiver pronto, até dar o numero de jogos do usuario
    cont += 1
print('----------BOA SORTE-----------')