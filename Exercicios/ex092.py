from datetime import datetime

pessoa = dict()

pessoa['nome'] = str(input('Nome: '))
ano = int(input('Ano nascimento: '))
pessoa['idade'] = datetime.now().year - ano
pessoa['clt'] = int(input('Numero Carteira de Trabalho (0 não tem): '))
if pessoa['clt'] == 0:
    print('-=' * 20)
    print(f'O nome é {pessoa['nome']}')
    print(f'A idade é {pessoa['idade']}')
    print(f'Não tem carteira de trabalho')
else:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    aposento = pessoa['contratação'] + 35
    pessoa['aposentar'] = aposento - ano
    pessoa['salario'] = float(input('Salário: '))
    print('-=' * 20)
    print(f'O nome é {pessoa['nome']}')
    print(f'A idade é {pessoa['idade']}')
    print(f'O numero da carteira de trabalho é {pessoa['clt']}')
    print(f'Ano de contratação é {pessoa['contratação']}')
    print(f'O seu salário é {pessoa['salario']}')
    print(f'Voce vai se aposentar com {pessoa['aposentar']} anos')
#ou posso mostrar assim também, mostrando as keys e os values do dicionário
#for k, v in pessoa.items():
#   print(f'{k} é {v}')