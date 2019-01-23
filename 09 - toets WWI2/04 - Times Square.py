def bereken_prijs(zin):
    plaats1 = zin.find('<')
    plaats2 = zin.find('>')
    nieuw = zin[:plaats1]
    kost = float(zin[plaats1 + 1:plaats2])
    prijs = float(len(nieuw) * kost)
    return nieuw, prijs

def toon_boodschappen(zin):
    tot_prijs = 0
    uitv = ''
    lengte = len(zin)
    while lengte != 0:
        boodschap, prijs = bereken_prijs(zin)
        tot_prijs += prijs
        plaats = 1 + zin.find('>')
        zin = zin[plaats:]
        uitv += boodschap
        lengte = len(zin)
        if lengte != 0:
            uitv += '\n'
    return str(tot_prijs) + '\n' + uitv

print(toon_boodschappen('I spent my last money on this billboard. Please give me a job.<2.68>Dear Emma, I love You more than words can say. Please wil you marry me?<2.42>I LOVE YOU AND WANT TO SPENT FOREVER WITH YOU. WILL YOU MARRY ME?<0.76>'))