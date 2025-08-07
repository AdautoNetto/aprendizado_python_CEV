nome = str(input('Digite o seu nome: ')).strip()
nma = nome.upper()
print('o Seu nome com todas as letras maiusculas: {}'.format(nma))

nmi = nome.lower()
print('O seu nome com todas as letras minusculas: {}' .format(nmi))

letra = len(nome) - nome.count(' ')
print('O seu nome tem {} letras'.format(letra))

separanome = nome.split()[0]

pn = len(separanome)
print('O seu  primeiro nome tem {} letras'.format(pn))
