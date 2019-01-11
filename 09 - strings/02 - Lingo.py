def hint(gok, teraden):
    uitv = ''
    for i in range(0, len(gok)):
        letter1 = gok[i]
        if letter1 == teraden[i]:
            uitv += letter1.upper()
        elif letter1 in teraden:
            uitv += letter1
        else:
            uitv += '.'
    return uitv