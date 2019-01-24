def versleutel_woord(woord, n):

    versleuteld_woord = ''

    woord = woord.upper()

    for letter in woord:

        versleutelde_letter = chr(ord(letter) + n)
        if versleutelde_letter == '@':
            versleutelde_letter = ' '

        versleuteld_woord += versleutelde_letter

    return versleuteld_woord

print(versleutel_woord('kaas?', 1))