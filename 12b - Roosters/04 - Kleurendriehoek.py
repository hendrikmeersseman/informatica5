def volgende_rij(rij):
    uitv = []
    for i in range(len(rij) - 1):
        if rij[i] == rij[i + 1]:
            uitv.append(rij[i])
        else:
            kleur = kleur_bepalen(rij[i], rij[i + 1])
            uitv.append(kleur)
    return uitv

def driehoek(lijst):
    uitv = []
    uitv.append(lijst)
    for i in range(len(lijst) - 1):
        lijst = volgende_rij(lijst)
        uitv.append(lijst)
    return uitv

def kleur_bepalen(kleur1, kleur2):
    lijst = ['Y', 'R', 'G']
    index = lijst.index(kleur1)
    lijst.pop(index)
    index = lijst.index(kleur2)
    lijst.pop(index)
    return ''.join(lijst)

def kleuren(lijst):
    groen, rood, geel = 0, 0, 0
    for i in range(len(lijst)):
        groen += lijst[i].count('G')
        rood += lijst[i].count('R')
        geel += lijst[i].count('Y')
    return groen, rood, geel


print(volgende_rij(['G', 'G', 'G', 'G', 'G']))
print(driehoek(['G', 'G', 'G', 'G', 'G']))
print(kleuren([['G', 'G', 'G', 'G', 'G'], ['G', 'G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G'], ['G']]))