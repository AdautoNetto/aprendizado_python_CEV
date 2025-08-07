def leiaInt(msg):
    #variavel local criada para verificar se a condição está correta=True, recebe falsa para entrar no looping
    ok = False
    valor = 0
    #estrutura de repetição criada para parar só quando o usuario digitar um numero correto
    while True:
        #variavel N recebe a variavel msg, esta em str as o padrão sem int é vir em str o formato
        n = str(input(msg))
        # condição if, se N for um numero, se ele for valor recebe a variavel n em formato de inteiro
        if n.isnumeric():
            valor = int(n)
            #variavel OK recebe True para acabar o código
            ok = True
        else:
            print('ERRO! Digite um numero inteiro válido')
        if ok:
            break
    return valor


#programa principal
n = leiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o número {n}')
