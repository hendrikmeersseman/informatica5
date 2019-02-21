def kleur_toevoegen(lijst, kleur):
    index = index_bepalen(kleur)
    lijst[index] += 1
    return lijst

def is_wit(lijst):
    return lijst[0] == lijst[1] == lijst[2]


def verf_verzamelen(lijst):
    nieuw, index = kleur_toevoegen([0, 0, 0], lijst[0]), 1
    while not is_wit(nieuw) and index < len(lijst):
        kleur_toevoegen(nieuw, lijst[index])
        index += 1
    if is_wit(nieuw):
        return index, nieuw

def index_bepalen(kleur):
    if kleur == 'rood':
        index = 0
    elif kleur == 'groen':
        index = 1
    elif kleur == 'blauw':
        index = 2
    return index

###################################################################################################################
print(kleur_toevoegen([3, 8, 8], 'rood'))
print(is_wit([2, 3, 2]))
print(verf_verzamelen(['rood', 'rood', 'blauw', 'blauw', 'rood', 'rood', 'rood', 'groen', 'blauw', 'groen', 'groen', 'groen', 'blauw', 'blauw', 'groen', 'blauw']))