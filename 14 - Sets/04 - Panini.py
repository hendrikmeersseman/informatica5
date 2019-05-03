def nog_niet_in_bezit(nieuw, boek):
    return nieuw not in boek

def controleren_wr_dubbel_is(dubbel)

def verzamel(nieuw, boek, dubbel):

    if nog_niet_in_bezit(nieuw, boek):
        boek.add(nieuw)
        return boek, dubbel

    if len(dubbel) == 0:
        dubbel
    stop, index = 0, 1
    while not stop:



print(verzamel('Bosmans',set(),{}))
print(verzamel('Weber',{'Bosmans'},{}))
print(verzamel('Bosmans',{'Weber', 'Bosmans'},{}))
