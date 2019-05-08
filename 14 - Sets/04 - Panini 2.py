def verzamel(kaart, boek, dubbel):
    lengte = len(boek)
    boek.add(kaart)
    if len(boek) != lengte:
        return boek, dubbel
    nieuw = {kaart}
    verder = 0
    for key, value in dubbel.items():
        if nieuw.issubset(value):

            sleutel = key
            verder = 1
    if verder:
        dubbel[sleutel].remove(kaart)
        if dubbel[sleutel] == set():
            dubbel.pop(sleutel)
        if sleutel + 1 in dubbel:
            dubbel[sleutel + 1].add(nieuw)
        else:
            dubbel[sleutel + 1] = nieuw
    else:
        if 1 in dubbel:
            dubbel[1].add(kaart)
        else:
            dubbel[1] = nieuw
    return boek, dubbel
