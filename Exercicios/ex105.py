def notas(*nota, sit=False):
    r = dict()

    totnotas = 0
    r['total'] = len(nota)
    r['maior'] = max(nota)
    r['menor'] = min(nota)
    for n in nota:
        totnotas += n
    r['media'] = totnotas / r['total']
    if r['media'] <= 5:
        r['situação'] = "Ruim"
    elif r['media'] <= 8:
        r['situação'] = 'Mediano'
    else:
        r['situação'] = 'excelente'

    return r


#programa principal
resp = notas(5.5, 2.5, 10, 6.5, sit=True)
print(resp)
