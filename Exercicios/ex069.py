idade, maior,homem, mulhermenor= 0, 0, 0, 0
sexo, continuar = '', ''
while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Digite sua idade: '))
    if idade >= 18:
        maior += 1

    sexo = str(input('Digite seu sexo: [M/F] ')).upper()[0]

    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Digite seu sexo: [M/F] ')).upper()[0]

    if sexo == 'M':
        homem += 1

    if sexo == 'F' and idade < 20:
        mulhermenor += 1

    continuar = str(input('Deseja continuar? [S/N] ')).upper()[0]

    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Deseja continuar? [S/N] ')).upper()[0]

    if continuar == 'N':
        break

print(f'{maior} pessoas com mais de 18 anos foram cadastradas.')
print(f'{homem} homens foram cadastrados.')
print(f'{mulhermenor} mulheres com menos de 20 anos foram cadastradas.')
