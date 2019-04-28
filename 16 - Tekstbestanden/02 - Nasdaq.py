def verwijder_newline(lijn):
    uitv = []
    for element in lijn:
        if '\n' in element:
            element = element[:-1]
            uitv.append(element)
        else:
            uitv.append(element)
    return uitv

def lees_bestand(file):
    with open(file) as bestand:
        bestand = bestand.readlines()
        nieuw = []
        for i in bestand:
            lijn = i.split(';')
            lijn = verwijder_newline(lijn)
            nieuw.append(lijn)
        return nieuw

def selecteer_kolom(rij, bestand):
    file = lees_bestand(bestand)
    index = file[0].index(rij)
    file.pop(0)
    uitv = []
    for element in file:
        uitv.append(float(element[index]))
    return uitv

def hoogste_koers(lijst):
    return max(lijst)

print(hoogste_koers(selecteer_kolom('High', 'Apple.txt')))