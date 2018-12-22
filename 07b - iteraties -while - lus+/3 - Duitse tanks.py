nummer = int(input('geef serienummer: '))
grootste = nummer
aantal = 0

while nummer > 0:
    if nummer > grootste:
        grootste = nummer
    aantal += 1
    nummer = int(input('geef serienummer: '))

#formule
totaal = (((aantal + 1) * grootste) / aantal) - 1
totaal = round(totaal)

#uitvoer
uitv = 'Het aantal geproduceerde tanks wordt geschat op ' + str(totaal) + '.'

print(uitv)