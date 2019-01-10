stop = 0
aantal_25 = 0
aantal_30 = 0
while not stop:
    temp = input('Geef temeratuur: ')
    if str(temp) == 'stop':
        stop = 1
    else:
        temp = float(temp)
        if temp >= 25:
            aantal_25 += 1
            if temp >= 30:
                aantal_30 += 1
        else:
            aantal_30, aantal_25 = 0, 0
        if aantal_30 >= 3 and aantal_25 >= 5:
            stop = 1

if aantal_25 >= 5 and aantal_30 >= 3:
    uitv = 'hittegolf'
else:
    uitv = 'geen hittegolf'

print(uitv)