def uur_en_minuten_nr_komma(uur, minuten):
    minuten = minuten * (5/3)
    uitv = uur + 0.01 * minuten
    if uitv > 24:
        uitv -= 24
    return uitv

tijd_vertrek_h = int(input('Geef uur van vertrek: '))
tijd_vertrek_m = int(input('Geef minuut van vertrek: '))
vertrek = uur_en_minuten_nr_komma(tijd_vertrek_h, tijd_vertrek_m)
print(vertrek)
tijd_aankomst_h = int(input('Geef uur van aankomst: '))
tijd_aankomst_m = int(input('Geef minuut van aankomst: '))
aankomst = uur_en_minuten_nr_komma(tijd_aankomst_h, tijd_aankomst_m)
print(aankomst)

tijd_vertrek2_h = int(input('Geef uur van vertrek2: '))
tijd_vertrek2_m = int(input('Geef minuut van vertrek2: '))
vertrek2 = uur_en_minuten_nr_komma(tijd_vertrek2_h, tijd_vertrek2_m)
print(vertrek2)

tijd_aankomst2_h = int(input('Geef uur van aankomst2: '))
tijd_aankomst2_m = int(input('Geef minuut van aankomst2: '))
aankomst2 = uur_en_minuten_nr_komma(tijd_aankomst2_h, tijd_aankomst2_m)

totaal = aankomst - vertrek
if totaal < 0:
    totaal += 24
vriendin = vertrek2 - aankomst
if vriendin < 0:
    vriendin += 24
rit = (totaal - vriendin) / 2
juiste = vertrek2 + rit

uur = int(juiste)
minuten = (juiste - uur) / (5/3)

print(uur)
print(minuten)