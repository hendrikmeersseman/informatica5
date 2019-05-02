def nog_niet_in_bezit(nieuw, boek):
    return nieuw not in boek


def verzamel(nieuw, boek, dubbel):
    if nog_niet_in_bezit(nieuw, boek):
        boek.add(nieuw)
        return boek, dubbel


print(verzamel('Bosmans',set(),{}))
print(verzamel('Weber',{'Bosmans'},{}))
