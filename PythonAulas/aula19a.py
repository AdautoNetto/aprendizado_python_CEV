estado = dict()
brasil = list()
#laço de repetição que vai guardar a entrada do usuario dentro de uma lista com a chave criada
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    #adicionando uma cópia do dicionário dentro de uma lista
    brasil.append(estado.copy())
#laço de repetição para mostrar cada dicionário inteiro
for e in brasil:
    print(e)
#laço de repetição para percorrer a minha lista
for e in brasil:
    #laço de repetição para percorrer o que está dentro da minha lista, que é o dicionário
    for k, v in e.items():
        print(f'{k} = {v}')
    print()
