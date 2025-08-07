from time import sleep


def maior(*numeros):
    maior_num, cont = 0, 0
    valores = list()
    valores.append(numeros)
    sleep(0.6)
    print('-=' *20)
    print('Analisando os valores passados...')
    sleep(0.5)
    for num in numeros:
        sleep(0.5)
        print(num, end = ' ')
    print(f'Foram informados {len(numeros)} valores ao todo')
    for n in numeros:
        if cont == 0:
            maior_num = n
        else:
            if n > maior_num:
                maior_num = n
        cont += 1
    print(f'O maior valor informado foi {maior_num}')


#programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
