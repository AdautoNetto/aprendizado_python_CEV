p = float(input('Qual é o seu peso em KG: '))
a = float(input('Qual é a sua altura em metros:'))

print('O seu peso em KG é: {:.2f} ' .format(p))
print('A sua altura em metros é: {:.2f} ' .format(a))

print('AGORA VOU CALCULAR O SEU IMC')
print('PROCESSANDO...')

imc = p / (a * a)

if imc < 18.5:
    print('Este não é o seu peso ideal, voce está magro.')
elif imc >= 18.5 and imc < 25:
    print('Este é o seu peso ideal, PARABÉNS !!!')
elif imc >= 25 and imc < 30:
    print('Este não é o seu peso ideal, voce está acima do peso')
elif imc >= 30 and imc < 40:
    print('Este não é o seu peso ideal, voce está obeso')
else:
    print('Voce é uma baleia')
