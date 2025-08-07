def soma(a=0, b=0, c=0):
    s = a + b + c
    return s


resp = soma(2, 3, 5)
print(f'A resposta da soma é: {resp}')

resp = soma(7, 8)
print(f'A resposta da soma é: {resp}')
#ou posso fazer assim
r1 = soma(6, 9, 2)
r2 = soma(8,2, 5)
r3 = soma(7, 8, 3)

print(f'as respostas das somas foram: {r1, r2, r3}')
