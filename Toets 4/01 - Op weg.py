def bestaat_weg(stad1, stad2, kaart):
    return {stad1}.issubset(kaart[stad2])

def geen_dubbelburen(stad1, stad2, kaart):
    buren1, buren2 = kaart[stad1], kaart[stad2]
    l1, l2 = buren1.difference(buren2), buren2.difference(buren1)
    uitv = l1.union(l2)
    return uitv.difference({stad1, stad2})

def bereikbaarheid_meest_afgelegen_stad(kaart):
    lijst = set()
    for value in kaart.values():
        lijst.add(len(value))
    return min(lijst)

def bestaat_route(steden, kaart):
    stad1 = steden[0]

    for index in range(1, len(steden)):
        stad2 = steden[index]
        if not bestaat_weg(stad1, stad2, kaart):
            return False
        stad1 = stad2
    return True


###################################################################################################################################
kaart = {'Brugge': {'Gent', 'Antwerpen'}, 'Kortrijk': {'Gent'}, 'Gent': {'Antwerpen', 'Kortrijk', 'Brugge'}, 'Antwerpen': {'Gent', 'Brussel', 'Brugge'}, 'Brussel': {'Hasselt', 'Antwerpen'}, 'Hasselt': {'Brussel'}}

print(bestaat_weg('Brussel', 'Hasselt', kaart))
print(bestaat_weg('Antwerpen', 'Kortrijk', kaart))
print(geen_dubbelburen('Brussel', 'Hasselt', kaart))
print(geen_dubbelburen('Antwerpen', 'Kortrijk', kaart))
print(bereikbaarheid_meest_afgelegen_stad(kaart))
print(bestaat_route(['Hasselt', 'Brussel', 'Antwerpen', 'Brugge', 'Gent', 'Kortrijk'], kaart))
