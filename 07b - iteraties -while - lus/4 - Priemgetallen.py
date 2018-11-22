getal = int(input('Welk getal wilt u onderzoeken? '))
n = 2
i = 1
gevonden = 1
while gevonden and n < getal:
    if (getal % n)  == 0:
        mes = '{} is geen priemgetal'.format(getal)
        i = 0
        gevonden = 0
    n += 1
if i and getal != 1:
    mes = '{} is een priemgetal'.format(getal)
elif getal == 1:
    mes = '1 is geen priemgetal'
print(mes)
