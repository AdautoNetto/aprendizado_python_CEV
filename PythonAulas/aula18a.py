galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
# para mostrar a lista primária inteira
print(f'para mostrar a lista primária inteira: {galera}')
# para mostrar somente uma lista secundaria especifica
print(f'para mostrar somente uma lista secundaria especifica: {galera[0]}')
# para mostar uma lista secundaria e de dentro dessa lista mostrar um elemento dela
print(f'para mostar uma lista secundaria e de dentro dessa lista mostrar um elemento dela: {galera[0][1]}')
# para mostrar cada lista secundaria da minha lista primaria
for pessoa in galera:
    print(pessoa)
# para mostrar cada elemento da lista secundaria da minha lista primaria
for pessoa in galera:
    print(f'Nome: {pessoa[0]}')
    print(f'Idade: {pessoa[1]}')
