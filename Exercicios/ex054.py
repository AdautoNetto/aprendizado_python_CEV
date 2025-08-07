import datetime

pm = 0
pmo = 0
for c in range(1, 4):
    p = int(input('Digite o ano de nascimento da {}° pessoa: ' .format(c)))
    if datetime.date.today().year - p < 18:
        pm += 1
    else:
        pmo += 1
print('{} pessoa(s) são de maior'.format(pmo))
print('{} pessoa(s) são de menor'.format(pm))