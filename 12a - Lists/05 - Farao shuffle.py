def nieuw_kaartspel(kleuren, cijfers):
    uitv = []
    for i in kleuren:
        for element in cijfers:
            uitv += [i + element]
    return uitv

def splits_kaartspel(lijst):
    lijst1 = lijst[:len(lijst) // 2]
    lijst2 = lijst[len(lijst) // 2:]

    return lijst1, lijst2

def faro_shuffle(lijst1, lijst2):
    uitv = []
    for i in range(len(lijst1)):
        uitv.append(lijst1[i])
        uitv.append(lijst2[i])

    if len(lijst2) > len(lijst1):
        uitv.append(lijst2[-1])
    return uitv


print(nieuw_kaartspel(['dood ', 'liefde ', 'tijd '], ['0', '1']))
print(splits_kaartspel(['dood 0', 'dood 1', 'liefde 0', 'liefde 1', 'tijd 0', 'tijd 1']))






