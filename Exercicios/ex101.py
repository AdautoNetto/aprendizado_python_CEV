def voto(ano=0):
    import datetime
    i = datetime.date.today().year - nascimento
    if i <= 15:
        print(f'Com {i} anos voce NÃO pode votar')
    elif i < 18 and i >= 16:
        print(f'Com {i} anos o voto é OPCIONAL')
    elif i >= 18 and i < 65:
        print(f'Com {i} anos o voto é OBRIGATÓRIO')
    else:
        print(f'Com {i} anos o voto é OPCIONAL')



#programa principal
print('-' *20)
nascimento = int(input('Em que ano voce nasceu: '))
voto(nascimento)
