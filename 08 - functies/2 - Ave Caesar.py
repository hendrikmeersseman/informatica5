def is_letter(letter):
    nummer = ord(letter)
    if 64 < nummer < 91 or 96 < nummer < 123:
        uitv = True
    else:
        uitv = False
    return uitv

def roteer_letter(letter, plaatsen):
    plaatsen %= 26
    if is_letter(letter):
        nummer = ord(letter)
        if 64 < nummer < 91:
            nummer += plaatsen
            if nummer > 91:
                nummer -= 26
        elif 96 < nummer < 123:
            nummer += plaatsen
            if nummer > 122:
                nummer -= 26
    uitv = chr(nummer)
    return uitv

def versleutel(zin, plaatsen):
    nieuwezin = ''
    for letter in zin:
        if is_letter(letter):
            nieuwezin += roteer_letter(letter, plaatsen)
        else:
            nieuwezin += letter
    return nieuwezin

zin = str(input('Welke zin wilt u encrypteren? '))
nummer = int(input('Geef geheime versleuteling:'))
mes = versleutel(zin, nummer)
print(mes)