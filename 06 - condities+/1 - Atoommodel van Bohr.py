#invoer
aantal_elektronen = int(input('aantal e elektronen: '))

#berekenig
if aantal_elektronen <= 2:
    print('De K-schil is de buitenste schil van een stabiel atoom met {} elektronen.'.format(aantal_elektronen))
elif aantal_elektronen <= 10:
    print('De L-schil is de buitenste schil van een stabiel atoom met {} elektronen.'.format(aantal_elektronen))
elif aantal_elektronen <= 28:
    print('De M-schil is de buitenste schil van een stabiel atoom met {} elektronen.'.format(aantal_elektronen))
elif aantal_elektronen <= 60:
    print('De N-schil is de buitenste schil van een stabiel atoom met {} elektronen.'.format(aantal_elektronen))
elif aantal_elektronen <= 92:
    print('De O-schil is de buitenste schil van een stabiel atoom met {} elektronen.'.format(aantal_elektronen))
elif aantal_elektronen <= 124:
    print('De P-schil is de buitenste schil van een stabiel atoom met {} elektronen.'.format(aantal_elektronen))
else:
    print('De Q-schil is de buitenste schil van een stabiel atoom met {} elektronen.'.format(aantal_elektronen))
