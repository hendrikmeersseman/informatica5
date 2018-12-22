getal = str(input('Geef te onderzoeken getal: '))
som = 0

for i in getal:
    som += int(i)

#deling
deling = int(getal) % som

if deling == 0:
    uitv = getal +' is een Harshadgetal'
else:
    uitv = getal +' is geen Harshadgetal'

print(uitv)