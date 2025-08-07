#função fatorial para calcular o numero que o usuario digitou
def fatorial(n, show=False):
    #docstrings, para documentar a minha função
    """
    calcular a fatorial de um numero ->
    parametro n -> obrigatório, pois é o numero que a função vai calcular
    parametro show -> opcional, se show for igual a True mostra a conta inteira, se não mostrar somente o resultado
    return > retorna o valor da fatorial do numero
    """
    # f recebe 1 para dar certo a multiplicação, ele vai ser o resultado
    f = 1
    #laço de repetição FOR para cada C em uma contagem de n(numero) até zero de 1 em 1
    for c in range(n, 0, -1):
        #se o parametro for igual a True ele mostra a conta se não somente o resultado
        if show == True:
            if c > 1:
                print(f'{c} X', end = ' ')
            else:
                print('=', end = ' ')
        #o resultado recebe ele mesmo vezes o cont
        f *= c
    return f

#programa principal
num = int(input('Digite um numero: '))
resp = (fatorial(num, show=True))
print(resp)
print(help(fatorial))
