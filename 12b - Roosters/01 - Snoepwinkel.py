def bereken_prijs(lijst):
    prijs = 0
    for item in lijst:
        prijs += item[-1]
    return prijs

def winkelbriefje(lijst):
    briefje = []
    for item in lijst:
        briefje.append(item[0])
    return briefje

def sorteer(lijst):
    from operator import itemgetter
    lijst.sort(key=itemgetter(1))
    return lijst


print(sorteer([('Lays Paprika', 3.94), ('Napoleon', 1.48), ('Milky Way', 3.64), ('M&M', 3.06), ('Crocky Zout', 3.62), ('Bounty', 1.86)]))
print(winkelbriefje([('Lays Paprika', 3.94), ('Napoleon', 1.48), ('Milky Way', 3.64), ('M&M', 3.06), ('Crocky Zout', 3.62), ('Bounty', 1.86)]))
print(bereken_prijs([('Lays Paprika', 3.94), ('Napoleon', 1.48), ('Milky Way', 3.64), ('M&M', 3.06), ('Crocky Zout', 3.62), ('Bounty', 1.86)]))
print(bereken_prijs([('Crocky Zout', 1.39)]))