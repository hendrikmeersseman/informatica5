def versleutel_woord(woord, plaats):
    nieuw = ''
    for letter in range(len(woord)):
        nieuwe_letter = woord[letter].upper()
        nieuw += chr(ord(nieuwe_letter) + plaats)
        if nieuw[letter] == '@':
            nieuw = nieuw[:letter] + ' ' + nieuw[letter + 1:]
        elif woord[letter] == ' ':
            nieuw = nieuw[:letter] + '@'
    return nieuw

def versleutel_zin(zin, plaats):
    nieuw = versleutel_woord(zin, plaats)
    return nieuw

print(versleutel_woord('Pe rsoon ;sgev ens', 5))