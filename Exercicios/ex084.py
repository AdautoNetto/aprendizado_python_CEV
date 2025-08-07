pessoas = []
pessoa = []
maiorpeso = 0
menorpeso = 0
escolha = 'S'
cont = 0

while escolha == 'S':
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    cont += 1
#condição IF se for a primeira pessoa cadastrada maior peso e menor peso recebe o peso
    if cont == 1:
        maiorpeso = pessoa[1]
        menorpeso = pessoa[1]
#condição se não for a primeira pessoa
    else:
#condição IF se pessoa[1] que é o peso for maior que maior peso. maior peso recebe pessoa[1]
        if pessoa[1] > maiorpeso:
            maiorpeso = pessoa[1]
#condição IF se pessoa[1] que é o peso for menor que menor peso. menor peso recebe pessoa[1]
        if pessoa[1] < menorpeso:
            menorpeso = pessoa[1]
    #adicionando uma cópia da lista pessoa que tem nome e peso dentro da lista pessoas
    pessoas.append(pessoa[:])
    #limpando a lista secundaria para poder pegar os dados da pessoa
    pessoa.clear()
    while True:
        escolha = str(input('Voce quer continuar [S|N]: ')).strip().upper()[0]
        if escolha == 'N':
            print('Encerrando o programa...')
            break
        elif escolha == 'S':
            break
        else:
            print('Voce digitou uma opção inválida, tente novamente.')

print(f'Ao todo, voce cadastrou {cont} pessoas')
print(f'Os maiores pesos foram: {maiorpeso}kg de', end ='')
#laço de repetição que vai ler a lista principal
for p in pessoas:
#condição IF se p[1] que é o peso for igual ao maior peso, mostro o p[0] da lista secundaria
    if p[1] == maiorpeso:
        print(f'[{p[0]}]', end=' ')
print(f'\nOs menores pesos foram: {menorpeso} de ', end='')
for p in pessoas:
    if p[1] == menorpeso:
        print(f'[{p[0]}]', end=' ')
