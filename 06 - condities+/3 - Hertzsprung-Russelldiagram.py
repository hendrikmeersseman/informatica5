#invoer
temp = float(input('geef temperatuur van de ster: '))
licht =float(input('Geef de lichtkrant van de ster: '))

#berekening
if licht > 10000:
    uit = 'superreuzen (a)'
elif licht > 1000:
    uit = 'superreuzen (b)'
elif licht > 100 and temp < 7500:
    uit = 'heldere reuzen'
elif licht > 10 and temp < 6000:
    uit = 'reuzen'
elif (licht < 0.01 and temp > 5000) or (licht < 0.0001 and temp > 3000):
    uit = 'witte dwergen'
else:
    uit = 'hoofdreeks'
#uitvoer
print(uit)