from random import randint, seed
def versluetelen(zin, getal):
    nieuwezin = ''
    seed(getal + 12)
    optelling = getal / randint(0,100)
    for i in zin:
        seed(getal)
        a = ord(i)
        plaatsen = randint(0,1000)
        i = chr(a + plaatsen)
        nieuwezin += i
        getal += optelling
    return nieuwezin
def ontsleutelen(zin, getal):
    nieuwezin = ''
    seed(getal + 12)
    optelling = getal / randint(0, 100)
    for i in zin:
        seed(getal)
        a = ord(i)
        plaatsen = randint(0, 1000)
        i = chr(a - plaatsen)
        nieuwezin += i
        getal += optelling
    return nieuwezin
a = 1
zin = str(input('Geef de zin: '))
while a:
    vraag = str(input('wilt u versleutelen(ja/nee): '))
    if vraag == 'ja':
        nummer = int(input('Geef versleutelings code: '))
        mes = versluetelen(zin, nummer)
        a = 0
    elif vraag == 'nee':
        vraag = str(input('wilt u ontsleutelen(ja/nee): '))
        if vraag == 'ja':
            nummer = int(input('Geef code'))
            mes = ontsleutelen(zin, nummer)
            a = 0


print(mes)