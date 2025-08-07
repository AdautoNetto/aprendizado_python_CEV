nome = str(input('Digite seu nome completo: ')) .strip()

partes = nome.split()

primeiro = partes[0]
print('O seu primeiro nome é: {}' .format(primeiro))

segundo = partes[1]
print('O seu segundo nome é {}' .format(segundo))

ultimo = partes[-1]
print('O seu ultimo nome é: {}' .format(ultimo))
