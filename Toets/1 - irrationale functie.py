# invoer
a = float(input('geef x: '))
from math import sqrt

# berekening
if a < 2:
    mes = '{:.2f} ∉ dom(f)'.format(a)
elif a == 2:
    mes = '{:.2f} is nulpunt van f'.format(a)
else:
    b = sqrt(a - 2)
    mes = 'f({:.2f}) = {:.2f}'.format(a, b)

# uitvoer
print(mes)
