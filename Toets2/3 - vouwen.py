#invoer
dikte = int(input('Geef dikte van het papier: '))
afst = int(input('Geef afstand tot hemellichaam: '))
aantal = 0
#berekening
while dikte < afst:
    dikte *= 2
    aantal += 1
uitv = 'Na {} keer vouwen bedraagt de dikte van het papier {} mm.'.format(aantal, dikte)

#uitvoer
print(uitv)
