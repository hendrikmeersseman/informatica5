bericht = str(input('Geef Twitterbericht: '))

for i in range(0, len(bericht)):
    if bericht[i] == '#':
        start = i + 1
        while bericht[i] != ' ':
            i += 1
        stop = i
        uitv = bericht[start:stop]
        print(uitv)