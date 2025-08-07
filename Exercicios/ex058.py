import random

print('Vou pensar em um numero entre 0 e 10. Tente adivinhar...')

ns = random.randint(0,10)
p = 1

r = int(input('Qual voce acha que foi: '))
while r != ns:
    p += 1
    if r < ns:
        r = int(input('mais... tente novamente: '))
    if r > ns:
        r = int(input('menos... Tente novamente: '))
if p <=3:
    print('Parabéns voce acertou em {} tentativa(s) !' .format(p))
elif p <= 6:
    print('voce acertou em {} tentativas, da pra melhorar !' .format(p))
elif p <= 9:
    print('Voce acertou em {} tentativas, voce é ruim !' .format(p))
else:
    print('Está com sorte no amor em... voce acertou em {} tentativas' .format(p))

