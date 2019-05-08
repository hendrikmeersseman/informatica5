def verzamel(nieuw, boek, dubbel):
    lengte = len(boek)
    boek.add(nieuw)
    if len(boek) != lengte:
        return boek, dubbel
    verder = False
    for key, value in dubbel.items():
        if {nieuw}.issubset(value):
            sleutel, verder = key, True
    if verder:
        dubbel[sleutel].remove(nieuw)
        if dubbel[sleutel] == set():
            dubbel.pop(sleutel)
        if sleutel + 1 in dubbel:
            dubbel[sleutel + 1].add(nieuw)
        else:
            dubbel[sleutel + 1] = {nieuw}
    else:
        if 1 in dubbel:
            dubbel[1].add(nieuw)
        else:
            dubbel[1] = {nieuw}
    return boek, dubbel
