#invoer
aantal_getallen = int(input('geef aantal getallen: '))
maxi = float(input('getal: '))
g = maxi
for i in range(aantal_getallen - 1):
     a = float(input('getal: '))
     if a > maxi:
          maxi = a
     g += a
gem = g / aantal_getallen

#uitvoer
print('Het grootste getal is {:.0f} en het gemiddelde is {:.2f}'.format(maxi, gem))