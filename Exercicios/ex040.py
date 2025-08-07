an = int(input('Digite o ano de nascimento: '))
aa = int(input('Digite o ano em que estamos: '))

idade = aa - an
print('A sua idade é: {}'.format(idade))
print('Agora vamos verificar a sua situação com o exército brasileiro...')
print('-----------------------------------------------------------------')

if idade < 18:
   f = 18 - idade
   print('Voce precisa se alistar para o exército daqui a {} ano(s).'.format(f))
elif idade == 18:
    print('Voce precisa se alistar.')
else:
    f = idade - 18
    print('voce deveria ter se alistado a {} ano(s).'.format(f))