def hoogtemeters(lijst):
    uitv = []
    for index in range(len(lijst) - 1):
        verschil = lijst[index + 1] - lijst[index]
        uitv.append(verschil)
    return uitv

def dalen_en_stijgen(lijst):
    dalend, stijgend = 0, 0
    for getal in lijst:
        if getal < 0:
            dalend += getal
        else:
            stijgend += getal
    return abs(dalend), stijgend


def Bereken(lijst):
    lijst = hoogtemeters(lijst)
    return dalen_en_stijgen(lijst)

####################################################################################

aantal = int(input('Hoeveel verschillende maximale en minimale hoogtes hebt u bereikt? '))
lijst = []
for i in range(aantal):
    lijst.append(int(input('Geef max / min: ')))
dalen, stijgen = Bereken(lijst)


if dalen < 1000 and stijgen > 700:
    beoordeling = 'Uitstekend gefietst!!'
elif dalen > 900 and stijgen > 500:
    beoordeling = 'Goed gefietst!'
else:
    beoordeling = 'Dat kan beter!'


uitv = 'U hebt ' + str(dalen) + 'm afgedaalt en ' + str(stijgen) + 'm gestegen.' + '\n' + beoordeling
print(uitv)

#########################################################################################
print(hoogtemeters([822, 61, 347, 234, 883, 336]))
print(dalen_en_stijgen([-761, 286, -113, 649, -547]))