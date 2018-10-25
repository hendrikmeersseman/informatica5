#invoer
dv = float(input('dv: '))
vv = float(input('vv: '))
da = float(input('da: '))
va = float(input('va: '))

#berekening vrachtwagens
pv = min((vv * dv) / 40, 1)

#berekening auto's
pa = min((va * da) / 40, 1)

#berekening indicatoren
minp = min(pv, pa)
maxp = max(pv, pa)
verschp = abs(pv - pa)

# kleurcode berekenen
if minp > 0.7:
    mes = 'zwart'
elif maxp > 0.7 and verschp < 0.2:
    mes = 'rood'
elif verschp > 0.7:
    mes = 'geel'
else:
    mes = 'groen'

#uitvoer
print(mes)