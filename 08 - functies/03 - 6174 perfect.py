def splits(getal):
    d = getal % 10
    getal //= 10
    c = getal % 10
    getal //= 10
    b = getal % 10
    getal //= 10
    a = getal % 10
    return a, b, c, d

def oplopende_cijfers(a,b,c,d):
    s1 = min(a, b, c, d)
    s4 = max(a, b, c, d)

    #middenste getallen pebalen
    #het middenste van a,b,c is zeker niet s1 of s4
    k23 = max(min(a, b), min(b, c), min(a, c))
    k32 = a + b + c +d - s1 - s4 - k23

    #middenste getallen in volgorde plaatsen
    s2 = min(k23, k32)
    s3 = max(k23, k32)

    return s1, s2, s3, s4

def op_af_getallen(a,b,c,d):
    uitv = str(a) + str(b) + str(c) + str(d), str(d) + str(c) + str(b) + str(a)
    return uitv

def verschil(af,op):
    uitv = str(int(af) - int(op))
    while len(uitv) < 4:
        uitkomst = '0' + uitkomst

    return uitv

def kaprekar(getal):

    uitkomst = ''
    while getal != 6174:
        a, b, c, d = splits(getal)
        w, x, y, z = oplopende_cijfers(a, b, c, d)
        op, af = op_af_getallen(w, x, y, z)
        v = verschil(af, op)

        uitkomst += af + ' - ' + op + ' = ' + v

        getal = int(v)

        if getal != 6174:
            uitkomst += '\n'
    return uitkomst
print(kaprekar(int(input('Geef het getal die u wil testen: '))))

#a, b, c, d = splits(5342)
#w, x, y, z = oplopende_cijfers(a, b, c, d)
#op, af = op_af_getallen(w, x, y, z)
#v = verschil(af, op)
#print(op, af)