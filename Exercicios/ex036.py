vc =  float(input('Qual é o valor da casa: R$ '))
s = float(input('Qual é o valor do seu salário: R$ '))
a = int(input('Em quantos anos vai pagar: '))

vm = vc / (12 * a)
print('O valor mensal que voce ira pagar e de: R$ {:.2f}' .format(vm))

ps = (s * 30) / 100
print('30% De seu salário é: R$ {:.2f}'.format(ps))

if vm >= ps:
    print('Empréstimo recusado, pois o valor excedeu 30% do seu salário !!!')
else:
    print('Empréstimo aceito, parabéns !!!')