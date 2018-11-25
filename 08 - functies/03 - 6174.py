def splits(getal):
    getal = int(getal)
    getal1 = int(getal / 1000)
    getal2 = int((getal - getal1 * 1000 )/ 100)
    getal3 = int((getal - getal1 * 1000 - getal2 * 100) / 10)
    getal4 = int(getal - getal1 * 1000 - getal2 * 100 - getal3 * 10)
    return getal1, getal2, getal3, getal4

def oplopende_cijfers(g1, g2, g3, g4):
    alleg = g1, g2, g3, g4
    uitv = sorted(alleg)
    return tuple(uitv)

def op_af_getallen(getal):
    str
print(oplopende_cijfers(input()))