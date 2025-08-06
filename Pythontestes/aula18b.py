#para fazer uma lista dentro da outra e essa lista secundaria tem que ter mais de um elemento
galera = []
dados = []
totmaior, totmenor = 0, 0
for pessoa in range(0, 3):
#para pegar a resposta do usuario e colocar na lista dados
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
#para adicionar um cópia da lista dados que é a primeira pessoa
    galera.append(dados[:])
#para excluir a lista dados para o usuario digitar outra pessoa
    dados.clear()
print(galera)
#laço de repetição para verificar cada lista secundaria da minha lista principal
for pessoa in galera:
#condição IF se o segundo objeto da minha lista 2, que é a idade for menor que 21
    if pessoa[1] >= 21:
#para mostrar o primeiro objeto da minha lista 2, que é o nome da pessoa
        print(f'O {pessoa[0]} é maior de idade')
#para saber o total de maiores de idade
        totmaior += 1
    else:
        print(f'O {pessoa[0]} é menor de idade')
        totmenor += 1
print(f'O total de maiores de idade são: {totmaior}')
print(f'O total de menores de idade são: {totmenor}')