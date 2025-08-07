def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)
'''
-> calcula o aumento de um determinado valor, retornando o resultado com ou sem formatação.
param: preço = o preço que vou reajustar
param: taxa = qual é a porcentagem de aumento
param: formato = quer a saida formatada ou não ?
return: o valor reajustado, com ou sem formato
'''

def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if formato is False else moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if formato is False else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'. replace('.', ',')
