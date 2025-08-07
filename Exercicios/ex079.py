numeros = []
escolha = 'S'
#laço Enquanto escolha foi igual a S continua
while escolha == 'S':
#pede a entrada do usuario
    novo = (int(input('Adicione um valor: ')))
#verifica se o numero digitado está na lista criada, se não estiver ai adiciono
    if novo in numeros:
        print('Valor ja adicionado, não irei adicionar novamente...')
    else:
#comando para adicionar o numero a lista
        numeros.append(novo)
        print('Numero adicionado...')
#laço enquanto infinito, só para quando o usuario digita S
    while True:
        escolha = str(input('Voce quer continuar [S|N]: ')).strip().upper()[0]
        if escolha in 'SN':
#comandos break para para esse laço de repetição, pois o outro laço vai para ser for S              
            break
        else:
            continue
numeros.sort()
print(f'Os numeros digitados foram: {numeros}')
