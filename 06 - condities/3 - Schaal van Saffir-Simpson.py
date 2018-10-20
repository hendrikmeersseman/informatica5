#invoer
snelheid = float(input('winsnelheid: '))

#programma
if snelheid <= 118:
    print('geen orkaan')
elif 119 <= snelheid <= 153:
    print('categorie 1')
elif 154 <= snelheid <= 177:
    print('categorie 2')
elif 178 <= snelheid <= 209:
    print('categorie 3')
elif 210 <= snelheid <= 249:
    print('categorie 4')
else:
    print('categorie 5')