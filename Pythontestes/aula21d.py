def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


#programa principal
num = int(input('Digite um valor: '))
if par(num):
    print('é par ')
else:
    print('é impar ')
