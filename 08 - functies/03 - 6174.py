def splits(getal):
    getal = int(getal)
    getal1 = int(getal / 1000)
    getal2 = int((getal - getal1 * 1000) / 100)
    getal3 = int((getal - getal1 * 1000 - getal2 * 100) / 10)
    getal4 = int(getal - getal1 * 1000 - getal2 * 100 - getal3 * 10)
    return getal1, getal2, getal3, getal4

def oplopende_cijfers(g1, g2, g3, g4):
    alleg = g1, g2, g3, g4
    uitv = tuple(sorted(alleg))
    return uitv

def op_af_getallen(g1, g2, g3, g4):
    opgetal = str(str(g1) + str(g2) + str(g3) + str(g4))
    afgetal = str(str(g4) + str(g3) + str(g2) + str(g1))
    return opgetal, afgetal

def verschil(af, op):
    uitv = int(af) - int(op)
    return str(uitv)

def kaprekar(getal):
    g1, g2, g3, g4 = splits(getal)
    op = oplopende_cijfers(g1, g2, g3, g4)
    op2 = ''.join(map(str, op))
    sp1, sp2, sp3, sp4 = splits(op2)
    opgetal, afgetal = op_af_getallen(sp1, sp2, sp3, sp4)
    versch = verschil(afgetal, opgetal)
    uitv = str(afgetal) + ' - ' + str(opgetal) + ' = ' + str(versch)
    getal = versch
    while int(getal) != 6174:
        g1, g2, g3, g4 = splits(getal)
        op = oplopende_cijfers(g1, g2, g3, g4)
        op2 = ''.join(map(str, op))
        sp1, sp2, sp3, sp4 = splits(op2)
        opgetal, afgetal = op_af_getallen(sp1, sp2, sp3, sp4)
        versch = verschil(afgetal, opgetal)
        uitv = uitv + '\n' + str(afgetal) + ' - ' + str(opgetal) + ' = ' + str(versch)
        getal = versch
    return uitv

getal = int(input('Geef een geta waarop je kaprekar wil toepassen: '))
g1, g2, g3, g4 = splits(getal)
if len(str(getal)) != 4:
    uitv = 'Hierop kan kaprekar niet toegepast worden!'
elif g1 == g2 == g3 == g4:
    uitv = 'Dit getal komt uit op 0'
else:
    uitv = kaprekar(getal)
print(uitv)
