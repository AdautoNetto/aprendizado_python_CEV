def area(l, c):
    a = l * c
    print(f'A area de um terreno de {largura}X{comprimento} em metros é {a}M')

print('CONTROLE DE TERRENOS')
print('-' *20)

largura = float(input('Digite a LARGURA do terreno em metros: '))
comprimento = float(input('Digite o COMPRIMENTO do terreno em metros: '))

area(largura, comprimento)