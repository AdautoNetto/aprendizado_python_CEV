ni = int(input('Digite um numero inteiro para fazer a conversão: '))
print('Agora escolha em qual base numérica quer converter')
print('[1] Binário')
print('[2] Octal')
print('[3] Hexadecimal')
e = (int(input('Digite o numero da sua opção para fazer a conversão: ')))

if e == 1:
    ncb =  bin(ni)[2:]
    print('O numero que voce escolheu convertido em binário é: {} ' .format(ncb))
elif e == 2:
    nco = oct(ni)[2:]
    print('O numero que voce escolheu convertido em octal é: {} ' .format(nco))
else:
    nco = hex(ni)[2:]
    print('O numero que voce escolheu convertido em hexadecimal é: {} ' .format(nco))
