def wisselen_mogelijk(ruilmarkt, gewenst, verzameld):
    prijs = ruilmarkt[gewenst]
    lijst = set(verzameld)
    return prijs.issubset(lijst)

def bereken_ruilmiddelen(ruilmarkt, gewenst):
    uitv = {}
    for element in gewenst:
        for materiaal in ruilmarkt[element]:
            if materiaal in uitv:
                uitv[materiaal] += 1
            else:
                uitv[materiaal] = 1
    sorted(uitv)
    return uitv

def wisselen(ruilmarkt, gewenst, verzameld):
    if not wisselen_mogelijk(ruilmarkt, gewenst, verzameld):
         return verzameld
    for element in ruilmarkt[gewenst]:
        verzameld.remove(element)

    verzameld.append(gewenst)
    return verzameld
ruilmarkt = {'goud': {'wol', 'steen', 'erts'}, 'wol': {'hout', 'steen', 'erts'}, 'erts': {'hout', 'steen'}, 'steen': {'hout', 'graan'}}



#print(wisselen(ruilmarkt, 'wol', ['graan', 'erts', 'steen', 'steen', 'erts', 'erts', 'hout', 'goud']))