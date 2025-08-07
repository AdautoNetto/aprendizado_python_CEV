import datetime

print('--CLASSIFICANDO ATLETAS--')
ano = int(input('Qual a sua data de nascimento: '))

idade = datetime.date.today().year - ano

print('A sua idade é: {}'.format(idade))

if idade <= 9:
    print('Voce é um atleta mirim')
elif idade <= 14:
    print('Voce é um atleta infantil')
elif idade <= 19:
    print('Voce é um atleta junior')
elif idade <= 25:
    print('Voce é um atleta senior')
else:
    print('Voce é um atleta master')