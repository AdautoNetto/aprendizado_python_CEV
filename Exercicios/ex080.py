lista = []
#laço FORA para o usuario digitar o valor 5 vezes
for cont in range(0,5):
    numero = int(input('Digite um valor: '))
#condição IF se for o primeiro valor digitado ou o numero digitado for maior que o ultimo valor da lista
#adicionar o numero no final da lista
    if cont == 0 or numero > lista[-1]:
        lista.append(numero)
        print('adicionado ao final da lista...')
# se ele não for o primeiro valor e nem maior que o ultimo valor
    else:
#criando uma variavel para verificar a lista
        pos = 0
#laço While para enquanto a variavel pos for menor que o indice final da lista
        while pos < len(lista):
#condição IF se o numero digitado for menor ou igual a variavel pos, que está lendo do começo da lista até o final
            if numero <= lista[pos]:
#comandos para adicionar o numero digitado na posição que a variavel pos parou
                lista.insert(pos, numero)
                print(f'Adicionado na posição {pos}...')
                break
            pos += 1
print(f'Os valores digitados em ordens foram: {lista}')
