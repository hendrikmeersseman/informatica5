#invoer
snelheid_s = int(input('Snelheid Stijn: '))
snelheid_k = int(input('Snelheid Kaat: '))
afstand = int(input('Afstand tussen beide: '))
tijd = 1
som = snelheid_k + snelheid_s

#berekening
while som < afstand:
    tijd += 1
    som += snelheid_s + snelheid_k

#uitvoer
mes = 'Na {} s hebben Stijn en Kaat elkaar ontmoet.'.format(tijd)
print(mes)
