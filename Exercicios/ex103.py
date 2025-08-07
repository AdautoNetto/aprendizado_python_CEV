def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')

#programa principal
print('-' *20)
n = str(input('Nome do Jogador: '))
g = input('Numero de Gols: ')
#verfica se a variavel foi digitada por numero
if g.isnumeric():
    g = int(g)
else:
    g = 0
#verifica se retirando os espaço a variavel n fica vazia, se ficar somente o parametro gols da função ficha recebe valor
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
