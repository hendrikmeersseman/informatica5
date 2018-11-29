from random import randint, seed
def versluetelen(zin, getal, getal2):
    nieuwezin = ''
    seed(getal + getal2)
    optelling = getal / randint(0,100)
    for i in zin:
        seed(getal)
        a = ord(i)
        plaatsen = randint(0,1000)
        i = chr(a + plaatsen)
        nieuwezin += i
        getal += optelling
    return nieuwezin
def ontsleutelen(zin, getal, getal2):
    nieuwezin = ''
    seed(getal + getal2)
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
        nummer1, nummer2 = int(input('Geef versleutelings code: ')),int(input('Geef versleutelings code: '))
        mes = versluetelen(zin, nummer1, nummer2)
        a = 0
    elif vraag == 'nee':
        vraag = str(input('wilt u ontsleutelen(ja/nee): '))
        if vraag == 'ja':
            nummer1, nummer2 = int(input('Geef versleutelings code: ')), int(input('Geef versleutelings code: '))
            mes = ontsleutelen(zin, nummer1, nummer2)
            a = 0


print(mes)