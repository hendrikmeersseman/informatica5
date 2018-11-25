import time
def test(getal):
    getal = int(getal + 1)
    aantal = int(getal)
    for i in range(aantal):
        getal -= 1
        round(getal, 1)
        print(getal)
        time.sleep(1)
    print('Gelukkig Nieuwjaar!!')

test(int(input('Geef: ')))