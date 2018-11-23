import time
def test(getal):
    getal = int(getal + 1)
    aantal = int(getal / 0.1)
    for i in range(aantal):
        getal -= 0.1
        round(getal, 1)
        print(getal)
        time.sleep(0.1)
    print('Gelukkig Nieuwjaar!!')

test(int(input('Geef: ')))