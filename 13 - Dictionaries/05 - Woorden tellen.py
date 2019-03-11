def woord_frequentie(zinnen):
    zinnen = zinnen.lower()
    lijst, uitv = zinnen.split(), {}
    for element in lijst:
        if element[-1] == ',' or element[-1] == '.':
            lijst[lijst.index(element)] = element[:-1]
    for element in lijst:
        if element not in uitv:
            uitv[element] = 1
        else:
            uitv[element] += 1
    return uitv

def woorden_per_frequentie(zinnen):
    lijst, uitv = woord_frequentie(zinnen), {}
    for element in lijst:
        if lijst[element] in uitv:
            uitv[lijst[element]].append(element)
        else:
            uitv[lijst[element]] = [element]
    return uitv

def meest_gebruikte_woorden(zinnen):
    verzameling = woorden_per_frequentie(zinnen)
    return verzameling[max(verzameling)]

##########################################################################################"""
print('ik ben blij'.split())
print(woord_frequentie('Dit is een zin. En nog een zin. En een laatste zin.'))
print(woorden_per_frequentie('Dit is een zin. En nog een zin. En een laatste zin.'))
print(meest_gebruikte_woorden('Dit is een zin. En nog een zin. En een laatste zin.'))


