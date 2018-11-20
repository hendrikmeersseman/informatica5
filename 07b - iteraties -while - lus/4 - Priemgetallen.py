getal = int(input('Van welk getal wilt u weten of het een priemgetal is? '))
n = 2
i = 1
b = 1
if getal % 2 == 0:
    mes = '{} is geen priemgetal'.format(getal)
    b = 0
    i = 0
while b and n < getal:
    if (getal % n)  == 0:
        mes = '{} is geen priemgetal'.format(getal)
        i = 0
    n += 1
if i and getal != 1:
    mes = '{} is een priemgetal'.format(getal)
elif getal == 1:
    mes = '1 is geen priemgetal'
print(mes)
