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