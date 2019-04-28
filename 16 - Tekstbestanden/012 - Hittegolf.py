def lijsten_nr_lijst(lijst):
    uitv = []
    for i in range(len(lijst)):
        for b in lijst[i]:
            uitv.append(int(b))
    return uitv


def bepaal_hittegolven(bestand):
    nieuw = []
    with open(bestand) as file:
        lijst = file.readlines()

    for lijn in lijst:
        nieuw.append(lijn[:-1].split())

    temp = lijsten_nr_lijst(nieuw)
    data, aantal_25_plus, aantal_30_plus, aantal = [], 0, 0, 0
    for i in range(len(temp)):
        # dagen groter dan 25
        if temp[i] >= 25:
            aantal_25_plus += 1
            if temp[i] >= 30:
                aantal_30_plus += 1
        else:
            # was vorig periode hittegolf
            if aantal_25_plus >= 5 and aantal_30_plus >= 3:
                begin = (i - aantal_25_plus) + 1
                data.append((begin, i))
                aantal += 1
            aantal_30_plus, aantal_25_plus = 0, 0

    if aantal_30_plus >= 5 and aantal_30_plus >= 3:
        data.append((i + 1 - aantal_25_plus, i))

    return aantal, data

inv = str(input('Geef lijst met temperaturen: '))
print(bepaal_hittegolven(inv))