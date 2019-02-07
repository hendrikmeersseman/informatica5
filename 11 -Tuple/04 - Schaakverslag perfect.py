def geldige_zet(zet):
    #mes vermijden
    mes = False
    if len(zet) == 3 and zet[0] in 'KDTLP' and zet[1] in 'abcdefgh' and zet[2] in '12345678':
        mes = True
    elif len(zet) == 2 and zet[0] in 'abcdefgh' and zet[1] in '12345678':
        mes = True
    #mes vermijden
    #else:
        #mes = False
    return mes

def geldige_zetten(zetten):
    #while lus is beter!!
    i = 0
    while i < len(zetten) and geldige_zet(zetten[i]):
        i += 1
### gemakelijker returnen!!!!!!!!!
    return i == len(zetten)

print(geldige_zetten(('Ta1', 'e5', 'h8', 'f7', 'Db7', 'Lg3')))