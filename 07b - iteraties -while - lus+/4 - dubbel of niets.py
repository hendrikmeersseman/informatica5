kapitaal = int(input('Geef startkapitaal: '))
inzet = kapitaal
stop = 1
te_veel = 0
failliet = 0
#berekening
while stop and not te_veel and not failliet:
    #controleren op voldoende kapitaal
    if kapitaal > 0:
        #inzet vragen en controleren op stop

        inzet = str(input('inzet: '))
        if inzet == 'stop':
            stop = 0
        elif inzet == 'alles' or int(inzet) <= kapitaal:

            #inzet controleren
            if inzet == 'alles':
                inzet = kapitaal

            elif inzet == 'stop':
                stop = 0
            else:
                bedrag = int(inzet)

            #kleuren vragen
            kleur_1 = str(input('gegokt kleur'))
            kleur_2 = str(input('resulterend kleur'))

            #kleuren contorleren en prijs berekenen
            if kleur_1 == kleur_2 and stop:
                kapitaal -= int(inzet)
                kapitaal += 2 * int(inzet)
            else:
                kapitaal -= int(inzet)
        else:
            uitv = 'Je kunt geen ' + inzet + ' dollar inzetten als je maar ' + str(kapitaal) + ' dollar hebt.'
            te_veel = 1
    else:
        failliet = 1
#uitvoer voor einde met stop
if not stop and not te_veel and not failliet:
    uitv = 'Je eindigt met ' + str(kapitaal) + ' dollar.'

#uitvoer voor faillissement
elif failliet:
    uitv = 'Je eindigt met ' + str(kapitaal) + ' dollar.'

#uitvoer printen
print(uitv)