#Middagmaal: € 5.3
#Soep: € 1.7
#Vieruurtje: € 2.3
def maaltijdprijs(maaltijdtype, aantal):
    maaltijdprijs = 0
    if maaltijdtype == 'middagmaal':
        maaltijdprijs += aantal * 5.3
    elif maaltijdtype == 'soep':
        maaltijdprijs += aantal * 1.7
    elif maaltijdtype == 'vieruurtje':
        maaltijdprijs += aantal * 2.3
    return maaltijdprijs


def dagprijs(invoer):
    prijs = 0
    for i in range(0, len(invoer), 2):
        prijs += maaltijdprijs(invoer[i], invoer[i + 1])
    return prijs

def weekprijs(invoer):
    prijs = 0
    for element in invoer:
        prijs += dagprijs(element)
    return prijs







dagprijs(('middagmaal', 2, 'soep', 2, 'vieruurtje', 2))
print(dagprijs(('middagmaal', 2, 'soep', 2, 'vieruurtje', 2)))