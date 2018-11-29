#invoer
hoeveel = int(input('Hoeveel basen? '))
allebasen = ''
aantal = 0

#berekening
for i in range(hoeveel):
    base = str(input('Geef base: '))
    if base not in allebasen:
        allebasen += base + ' '
        aantal += 1

if len(allebasen) <= 3:
    mes = 'De DNA-keting bevat 1 soort base: ' + allebasen
else:
    versch_b = len(allebasen) - aantal
    mes = 'De DNA-keting bevat ' + str(versch_b) + ' verschillende soorten basen: ' + allebasen

#uitvoer
print(mes)
