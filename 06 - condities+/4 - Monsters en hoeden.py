#invoer
p1 = str(input('kleur hoed persoon 1: '))
p2 = str(input('kleur hoed persoon 2: '))
leugen = float(input('persoon die liegt: '))

#berekening
if leugen == 1:
    if p1 == 'zwart' and p2 == 'zwart':
        print('wit')
        print('zwart')
    elif p1 == 'wit' and p2 == 'zwart':
        print('wit')
        print('wit')
    elif p1 == 'zwart' and p2 == 'wit':
        print('zwart')
        print('zwart')
    else:
        print('zwart')
        print('wit')
else:
    if p1 == 'zwart' and p2 == 'zwart':
        print('zwart')
        print('wit')
    elif p1 == 'wit' and p2 == 'zwart':
        print('zwart')
        print('zwart')
    elif p1 == 'zwart' and p2 == 'wit':
        print('wit')
        print('wit')
    else:
        print('wit')
        print('zwart')

