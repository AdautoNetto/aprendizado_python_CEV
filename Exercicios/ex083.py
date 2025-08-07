expre = str(input('Digite uma expressão: '))
pilha = []
#laço de repetição para verificar cada simbolo da expressão
for simbolo in expre:
#condição if se o simbolo é igual a '(', se for adiciona na lista pilha
    if simbolo == '(':
        pilha.append('(')
#condição if se simbolo for igual a ')'
    elif simbolo == ')':
#condição if se dentro da lista pilha tiver '('
        if len(pilha) > 0:
#remove o '(' da lista pilha
            pilha.pop()
#condição if se dentro da lista pilha não tiver nada
        else:
#adiciona ')' na pilha
            pilha.append(')')
            break
#condição if se tiver algo dentro da lista pilha
if len(pilha) > 0:
    print('A sua expressão está errada')
else:
    print('A sua expressão está correta')