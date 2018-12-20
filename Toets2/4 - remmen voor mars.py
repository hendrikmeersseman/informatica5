#invoer
v_gewenst = float(input('gewenste snelheid: '))
v_raket = float(input('snelheid raket: '))
aantal = 0

#berekening
while v_raket > v_gewenst:
    v_raket -= (v_raket * 0.30)
    aantal += 1

#uitvoer
uitv = 'na {} rembewegingen is de snelheid {:.2f}'.format(aantal, v_raket)
print(uitv)