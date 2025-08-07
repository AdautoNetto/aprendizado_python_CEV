pn = float(input('Qual é o valor do produto: '))
op = int(input('Qual é a opção de pagamento:  '
               '\n[1] Dinheiro ou PIX '
               '\n[2] Débito '
               '\n[3] Cédito '
               '\n[4] Crédito parcelado '
               '\nDigite a Opção: '))
if op == 1:
    pf = pn - (pn * 10 / 100)
    print('O valor final do produto é: {:.2f}' .format(pf))
elif op == 2:
    pf = pn - (pn * 5 / 100)
    print('O valor final do produto é: {:.2f}' .format(pf))
elif op == 3:
    print('O valor final do prduto é: {:.2f}' .format(pn))
elif op == 4:
    pf = pn + (pn * 20 / 100)
    print('O valor final do produto é: {:.2f}' .format(pf))
else:
    print('ERRO, DIGITE UMA OPÇÃO DE 1 A 4 ')
