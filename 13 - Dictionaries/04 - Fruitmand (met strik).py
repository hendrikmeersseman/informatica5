def fruitmand_maken(lijst):
    nieuw = {}
    for element in lijst:
        nieuw[len(element)] = element
    return nieuw

def fruitmand_inpakken(lijst):
    lengtes, nieuw = list(lijst), []
    lengtes.sort()
    for element in lengtes:
        nieuw.append(lijst[element])
    return nieuw


print(fruitmand_maken(['aardbei']))
print(fruitmand_maken(['banaan', 'aardbei', 'kiwi', 'peer', 'appel', 'bes', 'sinaasappel', 'framboos']))
print(fruitmand_inpakken({6: 'banaan', 7: 'aardbei', 4: 'peer', 5: 'appel', 3: 'bes', 11: 'sinaasappel', 8: 'framboos'}))