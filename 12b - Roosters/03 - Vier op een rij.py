def printbaar_rek(rek):
    rek.reverse()
    uitv = ''.join(rek[0])
    for i in range(1, len(rek)):
        uitv += '\n' + ''.join(rek[i])
    return uitv

def speel(kleur, kollom, rek):
    rek.reverse()
    stop = 0
    rij = 0
    while not stop and rij < len(rek):
        if rek[rij][kollom] != 'O':
            stop = 1
            rij -= 1
        rij += 1
    rek[rij - 1][kollom] = kleur
    rek.reverse()
    return rek


print(printbaar_rek([['R', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']]))
print(speel('G',3,[['R', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']]))
print( speel('G',1,[['R', 'R', 'R', 'R', 'G'], ['G', 'G', 'R', 'G', 'R'], ['O', 'G', 'O', 'O', 'O'], ['O', 'R', 'O', 'O', 'O']]))