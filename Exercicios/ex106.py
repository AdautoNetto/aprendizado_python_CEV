def pyhelp(cmd):
    from time import sleep
    sleep(0.5)
    help(f'{cmd}')
    sleep(0.5)


#programa principal
print('-' *25)
print('Sistema de ajuda pyHelp')
print('-' *25)
while True:
    comando = str(input('Função ou biblioteca > '))
    if comando != 'fim':
        pyhelp(comando)
    else:
        print('Voce escolheu sair...')
        break
