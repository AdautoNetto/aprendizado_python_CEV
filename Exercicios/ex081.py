numeros = []
escolha = 'S'

#laço de repetição WHILE enquanto a variavel escolha foi igual a S, para o usuario poder digitar quantas vezes
#quiser o valor
while escolha == 'S':
#entrada do usuario
    numero = int(input('Digite um valor: '))
#adiciona o numero na lista numeros
    numeros.append(numero)
#laço de repetição WHILE enquanto o usuario não digitar S ou N, não vai para de rodar
    while True:
        escolha = str(input('Voce quer continuar [S|N]: ')).strip().upper()[0]
        if escolha in 'SN':
            break
        else:
            continue
#comando len para ler quantos indices tem a lista
print(f'Foram digitados {len(numeros)} numeros')
#comandos para colocar a lista em ordem decrescente
numeros.sort(reverse=True)
print(f'A lista em modo decrescente é: {numeros}')
#se tiver 5 na lista então digita o primeiro print
if 5 in numeros:
    print('O valor 5 faz parte da lista e aparece ', end='')
    print(f'{numeros.count(5)} vezes')

else:
    print('O valor 5 não faz parte da lista')
