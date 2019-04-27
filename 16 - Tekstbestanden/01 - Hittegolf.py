
nieuw = []
def lijsten_nr_lijst(lijst):
    uitv = []
    for i in range(len(lijst)):
        for b in lijst[i]:
            uitv.append(int(b))
    return uitv

with open('temperaturen.txt') as bestand:
    lijst = bestand.readlines()

lijn = lijst[0].split()

for lijn in lijst:
    nieuw.append(lijn[:-1].split())
temp = lijsten_nr_lijst(nieuw)





data = []
aantal_25_plus = 0
aantal_30_plus = 0
totaal = []
aantal = 0

for i in range(len(temp)):

    #dagen groter dan 25
    if temp[i] >= 25:
        aantal_25_plus += 1
        if temp[i] >= 30:
            aantal_30_plus += 1

    else:
        #was vorig periode hittegolf
        if (aantal_25_plus + aantal_30_plus) >= 5 and aantal_30_plus >=3:
            begin = (i - aantal_25_plus) + 1
            data.append((begin, i))
            aantal += 1
        #periode op nul zetten
        aantal_30_plus, aantal_25_plus = 0,0

if (aantal_25_plus + aantal_30_plus) >= 5 and aantal_30_plus >=3:
    data.append((i + 1 - aantal_25_plus, i))




print(data)

