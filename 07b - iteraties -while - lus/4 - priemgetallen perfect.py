getal = int(input('getal: '))
from math import sqrt
#zolang je het niet kan delen door 2, 3, 4, 5, ... is het allicht een priemgetal

deler = 2

while getal % deler != 0 and getal != 1 and deler <= sqrt(getal):
    deler += 1
if deler == int(sqrt(getal)):
    mes = 'priemgetal'
else:
    mes = 'geen priemgetal'

print(mes)