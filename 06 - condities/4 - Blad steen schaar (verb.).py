#invoer
s1 = input('speler 1:')
s2 = input('speler 2:')

#REKENWERK
if s1 == s2:
    mes = 'onbeslist'
elif (s1 == 'blad' and s2 == 'steen') or (s1 == 'steen' and s2 == 'schaar') or (s1 == 'schaar' and s2 == 'blad'):
    mes = 'speler 1 wint'
else:
    mes = 'speler 2 wint'

#uitvoer
print(mes)
