f = str(input('Digite uma frase: ')).upper().strip()
fse = f.replace(' ', '')
print('A frase digitada é: {}'.format(f))
t = len(f)
ftf = fse[t::-1]
print('A frase de trás para frente é: {}' .format(ftf))

if ftf == fse:
    print('Essa frase é um PALINDROMO')
else:
    print('Essa frase NÃO é um PALINDROMO')
