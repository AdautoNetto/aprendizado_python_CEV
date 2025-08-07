aluno = []
alunos = []
#laço enquanto WHILE looping infinito
while True:
    nome  = (str(input('Nome:')))
    nota1 = (float(input('Nota 1:')))
    nota2 = (float(input('Nota 2:')))
    media = (nota1 + nota2) / 2
    aluno.append([nome, [nota1, nota2], media])
    escolha = str(input('Quer continuar [S|N]: ')).strip().upper()[0]
    if escolha in 'Nn':
        break

print('-=' *30)
print(f'{"NO.":<4} {"NOME":<10} {"MÉDIA":>8}')
print('-' *27)
for i, a in enumerate(aluno):
    print(f'{i:<4} {a[0]:<10} {a[2]:>8}')

while True:
    print('-' * 27)
    opc = int(input('Voce quer mostrar as notas de qual aluno (999 interrompe): '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(aluno) - 1:
        print(f'Notas de {aluno[opc][0]} são {aluno[opc][1]}')
print('-----VOLTE SEMPRE-----')