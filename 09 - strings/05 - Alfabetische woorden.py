def positie_laagste_ascii(tekst):
    laagst = ord(tekst[0])
    positie = 0
    for i in range(1, len(tekst)):
        rang = ord(tekst[i])
        if rang < laagst:
            laagst = rang
            positie = i
    return positie

def sorteer(tekst):
    nieuw = ''
    for i in range(len(tekst)):
        positie = positie_laagste_ascii(tekst)
        nieuw += tekst[positie]
        tekst = tekst[:positie] + tekst[positie + 1:]
    return nieuw

def is_alfabetisch(tekst):
    nieuw = sorteer(tekst)
    if tekst in nieuw:
        return True
    else:
        return False

