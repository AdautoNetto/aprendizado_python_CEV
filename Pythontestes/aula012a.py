nome = str(input('Qual é o seu nome: ')).strip().lower()
if nome == 'netto':
    print('Seu nome é muito lindo, {}' .format(nome))
elif nome == 'pedro' or nome == 'Dautin' or nome == 'Carlos':
    print('Seu nome é mais ou menos..., {}' .format(nome))
elif nome == 'adauto':
    print('Parabéns, o eu nome é o mais lindo de todos !!!')
else:
    print('Não gosto do seu nome...')