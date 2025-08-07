p = float(input('Digite o preço do produto: R$'))
d = (p * 5 / 100)
pt = p - d
print('o valor do produto com o desconto é de: R${:.2f}' .format(pt))
print('e o valor do desconto é de: R${:.2f}' .format(d))