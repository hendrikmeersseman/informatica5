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
        if lijst
print('ik ben blij'.split())
print(woord_frequentie('Dit is een zin. En nog een zin. En een laatste zin.'))


