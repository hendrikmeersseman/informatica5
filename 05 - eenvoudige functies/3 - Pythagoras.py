#invoer
a = float(input('geef a: '))
b = float(input('geef b: '))
from math import sqrt

#berekening
c = sqrt((a ** 2) + (b ** 2))

#uitvoer
print('In een rechthoekige driehoek met rechthoekszijden a = {:.2f} en b = {:.2f} is de schuine zijde {:.2f}'.format(a, b, c))