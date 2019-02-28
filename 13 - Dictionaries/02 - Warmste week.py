def gift_inschrijven(inschrijving, alle_klassen):
    if inschrijving[0] in alle_klassen:
        alle_klassen[inschrijving[0]] += inschrijving[1]
    else:
        alle_klassen[inschrijving[0]] = inschrijving[1]
    return alle_klassen

print(gift_inschrijven(('5WWI', 78.33),{'6WWI': 64.87, '6BI': 71.63, '5BI': 26.39, '5WWI': 82.68}))
print(gift_inschrijven(('5IN', 73.81),{'6WWI': 64.87, '6BI': 71.63, '5BI': 26.39, '5WWI': 232.48}))