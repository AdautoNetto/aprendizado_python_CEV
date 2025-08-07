caros, total,  preco, cont, menor_preco = 0, 0.0, 0.0, 0, 0.0
produto, continuar, barato = '', '', ''


while True:
    produto = str(input('Digite o nome produto: '))
    preco = float(input('Digite o preço do produto: '))

    cont += 1
    total += preco

    if preco > 1000:
        caros += 1

    if cont == 1:
        barato = produto
        menor_preco = preco

    if preco < menor_preco:
        barato = produto

    continuar = str(input('Deseja continuar? [S/N] ')).upper()[0]

    if continuar != 'S' and continuar != 'N':
        print('Voce digitou uma opção inválida. Tente novamente.')
        continuar = str(input('Deseja continuar? [S/N] ')).upper()[0]

    if continuar == 'N':
        break
print(f'O valor total da compra foi R${total:.2f}')
print(f'{caros} produtos foram mais de R$1000')
print(f'O produto mais barato foi {barato}')