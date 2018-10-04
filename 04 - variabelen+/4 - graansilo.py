#invoer waarden
b = float(input('geef breedte van het veld ( in m.): '))
l = float(input('geef hoogte van het veld (in m.): '))
c = float(input('opbrengst van het veld per hectare: '))
r = float(input('straal van de silo( in m.): '))
h = float(input('hoogte van de silo (in m.): '))
import math

#berekening
opbrengst_veld = (l * b) / 10000 * c
V_silo = (r **2) * math.pi * h


aantal_silos = math.ceil(opbrengst_veld / V_silo)
print(aantal_silos)