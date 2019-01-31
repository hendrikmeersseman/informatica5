def versleutel_woord(woord, n):

    versleuteld_woord = ''

    woord = woord.upper()

    for letter in woord:

        versleutelde_letter = chr(ord(letter) + n)
        if versleutelde_letter == '@':
            versleutelde_letter = ' '

        versleuteld_woord += versleutelde_letter

    return versleuteld_woord

def versleutel_zin(zin,getal):
    index_spatie = zin.find(' ')
    code = ''

    while index_spatie != -1:
        woord = zin[:index_spatie]
        zin = zin[index_spatie+1:]

        code += '@' + versleutel_woord(woord, getal)
        index_spatie = zin.find(' ')
    if len(zin) > 0:
        code += '@' + versleutel_woord(zin, getal)

    return code

print(versleutel_zin('De VS is al enkele weken in de ban van het datalek van Equifax.', 1))