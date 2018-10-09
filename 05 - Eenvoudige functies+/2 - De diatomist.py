#invoer
rk = float(input('straal kleine cirkel: '))
rg = float(input('straal grote cirkel: '))
from math import pi

#Berekenin
n = int(0.83 * (rg ** 2) / (rk ** 2) - 1.9)
opp_g_c = (rg ** 2) * pi
opp_k_c = (rk ** 2) * pi
procent = ((n * opp_k_c) / opp_g_c) * 100

#uitvoer
print('{} kleine cirkels bedekken {:.2f}% van de grote cirkel'.format(n, procent))