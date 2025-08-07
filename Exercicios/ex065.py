o = 'S'
cont, soma, media, maior, menor = 0, 0, 0, 0, 0
while o == 'S':
# pede o numero par ao usuario
    numero = int(input('Digite um numero: '))
# pergunta para o usuario se ela quer continuar
    o = str(input('Voce quer cotinuar: [S|N]')).upper()
    cont += 1
    soma += numero
    media = soma // cont
# verificação do maior e do menor numero
# se for a primeira vez do usuario digitando, automaticamente o menor numero recebe numero
    if cont == 1:
        menor = numero
    if numero < menor:
        menor = numero
    if numero > maior:
        maior = numero

print('Voce digitou {} numero(s)'.format(cont))
print('A Média desses numeros é: {}'.format(media))
print('o maior numero digitado foi {} e o menor foi {}'.format(maior, menor))