sexo = str(input('Por favor informe o seu sexo: [M|F] ')).upper()

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados inválidos. Digite o seu sexo corretamente: [M|F] ')).upper()

if sexo == 'M':
    print('O sexo digitado foi o sexo masculino.')
if sexo == 'F':
    print('O sexo digitado foi o sexo feminino.')

