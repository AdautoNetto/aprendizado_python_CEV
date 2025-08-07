print('-' *14)
print('DADOS PESSOAIS')
print('-' *14)

mediaidade = 0
somaidade = 0
idadehomem = 0
nomehomem = ''
mulheres = 0
menormulher = 0

for p in range(1, 5):
    print('DADOS DA {}° PESSOA'.format(p))
    n = str(input('Qual é o seu nome: ')).strip()
    i = int(input('Qual é a sua idade: '))
    s = str(input('Qual é o seu genero: [M/F] ')).upper()
    somaidade += i

    if p == 1 and s == 'M':
        idadehomem = i
        nomehomem = n
    if s == 'M' and i > idadehomem:
        idadehomem = i
        nomehomem = n

    if s == 'F' :
        mulheres += 1
        if i < 20:
            menormulher += 1

mediaidade = somaidade / 4
print('-' *18)
print('A média da idade do grupo é: {:.2f}' .format(mediaidade))
print('-' *18)
print('O homem mais velho tem {} anos e o nome dele é {}' .format(idadehomem, nomehomem))
print('-' *18)
print('nessa lista tem {} pessoa(s) do sexo Feminino e {} tem menos de 20 anos ' .format(mulheres, menormulher))