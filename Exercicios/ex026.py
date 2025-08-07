frase = str(input('Digite uma frase: '))
frase = frase.lower()

qvezes = frase.count('a')
print('Em sua frase a letra A aparece {} ' .format(qvezes))

pos = frase.find('a')+1
print('Em sua frase a letra A aparece a primeira vez na posição {}' .format(pos))

posu = frase.rfind('a')+1
print('Em sua frase a letra A aparece a ultima vez na posição {}' .format(posu))