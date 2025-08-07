def escreva():
    caracter = len(palavra) + 4
    print('-' * caracter)
    print(f'  {palavra}')
    print('-' * caracter)

# programa principal
escolha = 'S'

while escolha in 'Ss':
    palavra = str(input('Digite uma palavra: '))
    escreva()
    escolha = str(input('Quer continuar [S|N]: ')).strip().upper()[0]
