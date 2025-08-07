def contagem(inicio, fim, passo):
    print('-=' * 20)
    print(f'Vamos contar de {inicio} até {fim} de {passo} em {passo}')
    print('-=' *20)
#verifica se o passo é igual a 0, se for ele recebe 1
    if passo == 0:
        passo = 1
#verifica se a contagem é decrescente e se o passo é positivo, se for passo recebe ele negativo
    if inicio > fim and passo > 0:
        passo = -passo
#fazer a contagem
#verifica se passo é positivo, se for. enquanto inicio for menor ou igual mostrar inicio e inicio recebe ele
#mesmo mais passo
    if passo > 0:
        while inicio <= fim:
            print(inicio, end=' ')
            inicio += passo
        print()
    else:
        while inicio >= fim:
            print(inicio, end=' ')
            inicio += passo
        print()

#programa principal

contagem(0, 10, 1)

contagem(10, 0, -2)

print('-=' * 20)
print('Agora voce faz a contagem !!')
print('-=' * 20)
i = int(input('Inicio: '))
print('-=' * 20)
f = int(input('Fim: '))
print('-=' * 20)
p = int(input('Passo: '))
print('-=' * 20)

contagem(i, f, p)
