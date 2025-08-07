from time import sleep

alunos = list()



def cadastro_aluno(lista_alunos):
    sleep(0.5)
    aluno = dict()
    print('-' *35)
    print('  Vamos cadastrar um aluno agora')
    print('-' *35)

    while True:
        aluno['nome'] = input('Nome do Aluno: ')
        if aluno['nome'].strip() == '':
            print('Voce não digitou nenhuma entrada !')
            print('Por favor, digite apenas o nome do aluno')
        elif not aluno['nome'].isalpha():
            print('Voce digitou um numero no nome do aluno, isso não é valido')
            print('Por favor Digite apenas o nome do aluno com caracteres')
        else:
            break

    while True:
        aluno['sexo'] = str(input('sexo [M|F]: ')).upper().strip()
        if aluno['sexo'].strip() == '':
            print('Voce não digitou nenhuma entrada !')
            print('Por favor, digite apenas M (masculino) ou F (feminino) para a validação' )
        elif aluno['sexo'] not in 'MF':
            print(f" O sexo ({aluno['sexo']}) não é valido")
            print('Por favor, digite apenas M (masculino) ou F (feminino) para a validação')
        else:
            break

    while True:
        try:
            aluno['idade'] = int(input('Idade: '))
        except (ValueError):
            print('Voce digitou um valor inválido para a idade do aluno')
            print('Por favor digite apenas numeros inteiros')
        else:
            if aluno['idade'] <= 0:
                print('Digite uma idade válida')
            else:
                break

    while True:
        try:
            aluno['nota1'] = float(input('Primeira nota: '))
        except (ValueError):
            print('Voce digitou um valor inválido para a nota do aluno')
            print('Por favor digite apenas notas válidos (entre 0 a 10) ')
        else:
            if aluno['nota1'] < 0 or aluno['nota1'] > 10:
                print('voce digitou uma nota inválida')
                print('Por favor, digite apenas notas válidas (entre 0 e 10)')
            else:
                break

    while True:
        try:
            aluno['nota2'] = float(input('Segunda nota: '))
        except (ValueError):
            print('Voce digitou um valor inválido para a nota do aluno')
            print('Por favor, digite apenas notas válidas (entre 0 e 10)')
        else:
            if aluno['nota2'] < 0 or aluno['nota2'] > 10:
                print('voce digitou uma nota inválida')
                print('Por favor, digite apenas notas válidas (entre 0 e 10)')
            else:
                break

    aluno['media'] = (aluno['nota1'] + aluno['nota2']) / 2
    if aluno['media'] < 6:
        aluno['situação'] = 'REPROVADO'
    elif aluno['media'] < 7:
        aluno['situação'] = 'RECUPERAÇÃO'
    else:
        aluno['situação'] = 'APROVADO'

    lista_alunos.append(aluno.copy())
    aluno.clear()


def mostrar_relatorio(lista_de_alunos):
    sleep(0.5)
    if not lista_de_alunos:
        print('Ainda não foi cadastrado alunos')
        print('Por favor cadastre alunos para mostrar os relatórios')
    else:
        print('---RELATÓRIO DE ALUNOS---')
        for aluno in lista_de_alunos:
            print('-' * 30)
            print(f'Nome: {aluno["nome"]}')
            print(f'Média: {aluno["media"]:.2f}')
            print(f'Situação: {aluno["situação"]}')
            print('-' * 30)



def consulta_nome(lista_de_alunos):
    sleep(0.5)
    if not lista_de_alunos:
        print('Ainda não foi cadastrado alunos')
        print('por favor cadastre alunos para prosseguir')
    else:
        encontrado = False
        sleep(0.5)
        print('---CONSULTA POR NOME---')
        nome = str(input('Nome do aluno: '))
        for i, aluno in enumerate(lista_de_alunos):
            if nome.lower() == aluno['nome'].lower():
                print('-' *30)
                sleep(0.5)
                print(f"NOME: {aluno['nome']}")
                print(f"SEXO: {aluno['sexo']}")
                print(f"IDADE: {aluno['idade']}")
                print(f"PRIMEIRA NOTA: {aluno['nota1']}")
                print(f"SEGUNDA NOTA: {aluno['nota2']}")
                print(f"MÉDIA: {aluno['media']}")
                print(f"SITUAÇÃO: {aluno['situação']}")
                print('-' * 30)
                encontrado = True
                break
        if not encontrado:
            print(f'O nome {nome} que voce digitou não está cadastrado no nosso sistema')



def relatorio_escolar(lista_de_alunos):
    if not lista_de_alunos:
        print('Ainda não foi cadastrado alunos')
        print('Por favor cadastre alunos para mostrar os relatórios')
    else:
        tot_alunos = len(lista_de_alunos)
        print(f'Foi cadastrado {tot_alunos} alunos no total')

        soma = 0
        for aluno in (lista_de_alunos):
            soma += aluno['media']
        media_geral = soma / tot_alunos
        print(f'A média geral dos alunos é {media_geral:.2f}')

        alunos_acima_media = 0
        for aluno in (lista_de_alunos):
            if aluno['media'] > media_geral:
                alunos_acima_media +=1
        print(f'{alunos_acima_media} aluno(s) esta(o) acima da média geral')

        tot_mulher = 0
        for aluno in (lista_de_alunos):
            if aluno['sexo'] == 'F':
                tot_mulher += 1
        print(f'O total de mulheres cadastradas é {tot_mulher}')


#programa principal
while True:
    try:
        sleep(0.5)
        print('---MENU PRINCIPAL---')
        print('[1] Cadastrar aluno')
        print('[2] Mostrar relatório de todos os alunos')
        print('[3] Consultar relatório por nome')
        print('[4] Relatório da Escola')
        print('[5] Sair')
        escolha = int(input('Digite uma opção válida: '))
    except (ValueError):
        print('Voce digitou uma opção inválida')
        print('Por favor, digite novamente')
    else:
        if escolha == 1:
            cadastro_aluno(alunos)

        elif escolha == 2:
            mostrar_relatorio(alunos)

        elif escolha == 3:
            consulta_nome(alunos)

        elif escolha == 4:
            relatorio_escolar(alunos)

        elif escolha == 5:
            print('Voce escolheu sair do programa...')
            sleep(0.5)
            break
        else:
            print('Voce digitou uma opção inválida')
            print('Por favor digite uma opção entre 1 a 4')
