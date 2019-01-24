getal = int(input('Geef getal: '))
aantal = int(getal / 2) + 1
totaal = 0
uitv = ' '
for i in range(1, aantal):
    if getal % (i) == 0:
        totaal += (i)
        uitv += str(i) +' '
if totaal == getal:
    uitv = str(getal) + ' is een perfect getal en de delers zijn' + uitv
else:
    uitv = str(getal) + ' is geen perfect getal'

print(uitv)