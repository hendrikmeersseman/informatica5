#invoer waarden
b = float(input('geef breedte van het veld ( in m.): '))
l = float(input('geef hoogte van het veld (in m.): '))
c = float(input('opbrengst van het veld per hectare: '))
r = float(input('straal van de silo( in m.): '))
h = float(input('hoogte van de silo (in m.): '))
import math

#berekening
opbrengst_veld = (l * b) / 10000 * c
V_silo = (r ** 2) * math.pi * h


aantal_silos_tot = math.ceil((opbrengst_veld / V_silo))
aantal_silos_vol = int((opbrengst_veld / V_silo))
aantal_silos = float(opbrengst_veld / V_silo)

halfvolle = aantal_silos - aantal_silos_vol
if halfvolle > 0:
    hoogte_laatste = (halfvolle * V_silo) / (r ** 2 * math.pi)
else:
    hoogte_laatste = h
print(aantal_silos_tot)
print(hoogte_laatste)