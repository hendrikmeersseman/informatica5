#invoer
p_1 = input('blad, steen of schaar: ')
p_2 = input('blad, steen of schaar: ')
#berekening
if p_1 == p_2:
    print ('onbeslist')
elif p_1 == 'blad' and p_2 == 'steen':
    print('speler 1 wint')
elif p_1 == 'steen' and p_2 == 'schaar':
    print('speler 1 wint')
elif p_1 == 'schaar' and p_2 == 'blad':
    print('speler 1 wint')
else:
    print('speler 2 wint')
