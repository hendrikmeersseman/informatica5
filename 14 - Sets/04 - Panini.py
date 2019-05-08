def nog_niet_in_bezit(nieuw, boek):
    return nieuw not in boek

def controleren_wr_dubbel_is(dubbel):
    pass

def verzamel(nieuw, boek, dubbel):

    if nog_niet_in_bezit(nieuw, boek):
        boek.add(nieuw)
        return boek, dubbel

    if len(dubbel) == 0:
        dubbel[1] = {nieuw}
        boek = set(sorted(boek, reverse = True))
        return boek, dubbel
    stop, index, lijst = 0, 0, []
    for key, value in dubbel.items():
        lijst.append(key)
    while not stop:
        if nieuw in dubbel[lijst[index]]:
            dubbel.pop(lijst[index])
            dubbel[lijst[index] + 1] = {nieuw}
            stop = 1



    return boek, dubbel
print(verzamel('Scifo',{'Staelens', 'Bosmans', 'Weber', 'Scifo'},{3: {'Bosmans'}}))
print(verzamel('Bosmans',{'Bosmans', 'Weber'},{1: {'Bosmans'}}))


# print(verzamel('Bosmans',set(),{}))
# print(verzamel('Weber',{'Bosmans'},{}))
# print(verzamel('Bosmans',{'Weber', 'Bosmans'},{}))
print(verzamel('Bosmans',{'Weber', 'Bosmans'},{1: 'Bosmans'}))
print(verzamel('Bosmans',{'Bosmans', 'Weber'},{}))

