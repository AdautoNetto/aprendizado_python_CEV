num = [2, 5, 9, 1]
print(f'Mostrando a lista normal {num}')
#para alterar um elemento da minha lista
num[2] = 3
print(f'Mostrando a lista depois alterar o 9 para o 3 {num}')
#para adicionar um elemento no último indice da minha lista
num.append(7)
print(f'Mostrando a lista depois de adicionar o 7 no ultimo indice {num}')
#para adicionar um elemento em qualquer indice da minha lista
num.insert(2, 0)  #primeiro coloco o indice que eu quero adicionar e depois o elemento
print(f'Mostrando a lista depois de adicionar o 0 no indice 2 {num}')
#para remover o último elemento da minha lista
num.pop()
print(f'Mostrando a lista depois de remover o ultimo elemento {num}')
#para remover qualquer elemento da minha lista
num.pop(2)#indice do elemento que vou remover
print(f'Mostrando a lista depois de remover o elemento do indice 2 {num}')
#para organizar a minha lista de maneira crescente
num.sort()
print(f'A minha lista de maneira crescente: {num}')
#para organizar a minha lista de maneira decrescente
num.sort(reverse=True)
print(f'A minha lista de maneira decrescente: {num}')
#para saber quantos elementos tem na minha lista
print(f'Essa lista tem {len(num)} elementos')
#se tiver o elemento 4 dentro da minha lista remover ele
if 4 in num:
    num.remove(4)
else:
    print(f'Não achei o numero 4 {num}')