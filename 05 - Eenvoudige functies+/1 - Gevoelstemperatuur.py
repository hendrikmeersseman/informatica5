#invoer
t = float(input('Geef temperatuur: '))
w = float(input('Geef windsnelheid: '))

#berekening
r = 13.12 + 0.6215 * t + ((0.3965 * t - 11.37) * pow(w, 0.16))

#uitvoer
print(r)
