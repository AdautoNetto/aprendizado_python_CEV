
for c in range(1, 6):
    p = float(input('Digite o peso da {}° : ' .format(c)))
    if c == 1:
        map = p
        mep = p
    else:
        if p > map:
            map = p
        if p < mep:
            mep = p
print('O maior peso digitado foi: {:.2f}' .format(map))
print('O menor peso digitado foi: {:.2f}' .format(mep))