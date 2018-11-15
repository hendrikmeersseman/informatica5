getal = int(input('eerste kaart: '))
som = getal

while som < 21 and getal:
    getal = int(input('kaart: '))
    som += getal
if som == 21:
    mes = 'Gewonnen!'
elif som > 21:
    mes = 'Verbrand ({})'.format(som)
else:
    mes = 'Voorzichtig gespeeld ({})'.format(som)
print(mes)