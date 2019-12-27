#invoer
import math
r = float(input('Afstand satelliet en M aarde: '))
v = float(input('snelheid satelliet: '))
m = 398600.4418 * 10**9
# grote as
a = (m * r) / (2 * m - r * v ** 2)
#periode
p = 2 * math.pi * math.sqrt((a ** 3) / m)
p_uitv = p
#periode in dagen...
aantal_dagen = p // 86400
p -= aantal_dagen * 86400
aantal_uren = p // 3600
p -= aantal_uren * 3600
aantal_minuten = p // 60
#uitv
print("grote as: {} meter".format(a))
print("periode: {} seconden".format(p_uitv))
print("periode: {} dagen, {} uren en {} minuten".format(int(aantal_dagen), int(aantal_uren), int(aantal_minuten)))