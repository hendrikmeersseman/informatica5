def verwijder_newline(lijn):
    uitv = []
    for element in lijn:
        element = element.replace(',', '').replace('\n', '')
        uitv.append(element)
    return uitv

def lees_aandeel(file):
    with open(file) as bestand:
        bestand, nieuw = bestand.readlines(), []
        for i in bestand:
            lijn = verwijder_newline(i.split(';'))
            nieuw.append(lijn)
    return nieuw

def selecteer_kolom(rij, bestand):
    file = lees_aandeel(bestand)
    index = file[0].index(rij)
    file.pop(0)
    uitv = []
    for element in file:
        uitv.append(float(element[index]))
    return uitv

def hoogste_koers(lijst):
    return max(lijst)
