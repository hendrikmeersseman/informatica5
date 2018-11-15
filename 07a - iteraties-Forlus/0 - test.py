n = int(input('getal: '))
cijfers, ontbreken = '', ''

for i in range(1, 11):
    cijfers += str(n * i)
for c in '0123456789':
    if c not in cijfers:
        ontbreken += c
if len(ontbreken) == 0:
    print('Tafel van ' + str(n) + ' is een mooie tafel')
else:
    print('In de tafel van ' + str(n) + ' ontbre(e)k(t)en ' + ontbreken)
