constante_van_avagrado = 6.020 * (10 ** 23)
molaire_massa_s = 32.06

#invoer
aantal_deeltjes_in_mol = float(input('aantal deeltjes in S: '))

#berekening
massa_s = (molaire_massa_s * aantal_deeltjes_in_mol)
aantal_deeltjes = (aantal_deeltjes_in_mol * constante_van_avagrado)

#uitvoer
print(massa_s)
print(aantal_deeltjes)