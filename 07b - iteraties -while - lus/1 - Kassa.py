prijs = float(input('Eerste product: '))
totale_prijs = prijs

while prijs > 0:
    prijs = float(input('product: '))
    totale_prijs += prijs

print('De totale prijs is € {:.2f}'.format(totale_prijs))